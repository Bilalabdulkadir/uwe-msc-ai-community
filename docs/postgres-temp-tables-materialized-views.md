# Production Reference: Temp Tables, Materialized Views, CTEs, and Security-Restricted Operations in PostgreSQL

## Part 1: The Problem

### 1.1 Security-Restricted Operations and Materialized Views

When PostgreSQL executes the defining query of a materialized view (during `CREATE MATERIALIZED VIEW` or `REFRESH MATERIALIZED VIEW`), the query runs in a **security-restricted operation**. [1](https://www.postgresql.org/docs/14/sql-creatematerializedview.html)

PostgreSQL explicitly forbids operations that create temporary tables in this context.

#### Example of Failure

```sql
CREATE FUNCTION my_func()
RETURNS int
LANGUAGE plpgsql
AS $$
BEGIN
    CREATE TEMP TABLE t(x int);
    RETURN 1;
END;
$$;

CREATE MATERIALIZED VIEW mv AS
SELECT my_func();
```

Error:

```text
ERROR: cannot create temporary table within security-restricted operation
```

#### Why This Restriction Exists

Temporary tables affect session state: they appear in `pg_temp`, alter name resolution through the search path, and can cause unpredictable behavior if materialized-view refresh creates session-visible objects. [2](https://www.postgresql.org/message-id/CAFBoRzf6HwFg1jovdOrbtC6x4xKV__-t5EjSzbY2068S01pcTg%40mail.gmail.com)

### 1.2 This Is Specifically a Temp-Table Problem

**Clarification:**

The restriction is specific to temporary tables, not to VOLATILE functions generally.

Incorrect understanding:

> "Materialized views forbid VOLATILE functions."

Correct understanding:

> "Materialized views forbid operations that create temporary tables. VOLATILE functions that do not create temporary tables may be allowed, depending on other restrictions."

The PostgreSQL documentation and related discussions do not establish a blanket prohibition against VOLATILE functions inside materialized-view definitions. [1](https://www.postgresql.org/docs/14/sql-creatematerializedview.html)

---

## Part 2: The Solution Space

### 2.1 CTEs: What They Solve

A Common Table Expression (CTE) created with `WITH` is a temporary result set that exists only for the duration of a query. [3](https://www.postgresql.org/docs/current/queries-with.html)

#### Why CTEs Help

A CTE:

- Does not create schema objects.
- Does not modify session state.
- Automatically disappears at query completion.
- Is allowed inside materialized-view definitions.

#### What CTEs Do *Not* Solve

A CTE avoids the specific temp-table restriction. It does not prevent all restricted operations.

Example:

```sql
WITH step1 AS (
    SELECT *
    FROM source_table
)
SELECT dangerous_function()
FROM step1;
```

If `dangerous_function()` attempts another restricted operation, the query may still fail.

The benefit is narrow: CTEs replace temp tables themselves.

---

### 2.2 Basic CTE Pattern

```sql
CREATE OR REPLACE FUNCTION my_func()
RETURNS TABLE (
    id INT,
    result TEXT
)
LANGUAGE SQL
STABLE
AS $$
WITH step1 AS (
    SELECT
        id,
        data
    FROM source_table
),
step2 AS (
    SELECT
        id,
        upper(data) AS data
    FROM step1
)
SELECT
    id,
    data AS result
FROM step2;
$$;

CREATE MATERIALIZED VIEW some_view AS
SELECT *
FROM my_func();
```

### 2.3 Recursive Pattern

Use `WITH RECURSIVE` only when a CTE actually references itself.

```sql
CREATE OR REPLACE FUNCTION hierarchy_walk()
RETURNS TABLE (
    id INT,
    parent_id INT,
    data TEXT,
    depth INT
)
LANGUAGE SQL
STABLE
AS $$
WITH RECURSIVE hierarchy AS (
    -- Anchor: root nodes
    SELECT
        id,
        parent_id,
        data,
        1 AS depth
    FROM source_table
    WHERE parent_id IS NULL

    UNION ALL

    -- Recursive: descendants
    SELECT
        child.id,
        child.parent_id,
        child.data,
        parent.depth + 1
    FROM source_table child
    JOIN hierarchy parent
      ON child.parent_id = parent.id
)
SELECT
    id,
    parent_id,
    data,
    depth
FROM hierarchy;
$$;
```

Avoid using `WITH RECURSIVE` when recursion is not actually present. It works, but incorrectly signals intent.

---

## Part 3: Function Volatility

### 3.1 Volatility Categories

#### IMMUTABLE

Given the same arguments, always returns the same result.

No dependence on database contents, time, configuration, or external state.

```sql
CREATE FUNCTION format_name(first text, last text)
RETURNS text
LANGUAGE SQL
IMMUTABLE
AS $$
    SELECT concat(first, ' ', last);
$$;
```

#### STABLE

Returns the same value for identical inputs during a single statement.

A STABLE function may read tables. Table contents may change between statements, so the function is not IMMUTABLE.

```sql
CREATE FUNCTION get_user_name(p_user_id int)
RETURNS text
LANGUAGE SQL
STABLE
AS $$
    SELECT name
    FROM users
    WHERE id = p_user_id;
$$;
```

#### VOLATILE

May return different values on every invocation.

Examples:

```sql
random()
clock_timestamp()
nextval()
```

VOLATILE functions may perform writes.

### 3.2 SQL-Language Functions Can Modify Data

SQL-language functions are not inherently read-only.

A VOLATILE SQL-language function may execute modifying statements.

```sql
CREATE FUNCTION log_event(
    p_type text,
    p_details text
)
RETURNS void
LANGUAGE SQL
VOLATILE
AS $$
    INSERT INTO event_log (
        event_type,
        details,
        created_at
    )
    VALUES (
        p_type,
        p_details,
        now()
    );
$$;
```

Do not assume:

- LANGUAGE SQL → read-only
- LANGUAGE plpgsql → writable

The capability depends on the statements executed.

### 3.3 Volatility and Materialized Views

When a function is used in a materialized-view definition:

- IMMUTABLE functions are safest.
- STABLE functions are generally acceptable.
- VOLATILE functions that do not create temporary tables may work, depending on other constraints.

The primary concern is whether the function's result is stable enough to justify materialization, not whether the function's volatility classification alone forbids its use.

---

## Part 4: CTE Materialization

### 4.1 CTE Inlining (PostgreSQL 12+)

By default, PostgreSQL inlines CTEs—that is, it merges them into the outer query.

```sql
-- Inlined (single pass)
WITH t AS (
    SELECT id, expensive_func(data) AS computed
    FROM source_table
)
SELECT * FROM t;
```

Inlining allows optimizations such as predicate pushdown.

### 4.2 Multiple References and Materialization

When a CTE is referenced multiple times, PostgreSQL may materialize it automatically to avoid repeated computation.

To force materialization explicitly:

```sql
WITH expensive AS MATERIALIZED (
    SELECT
        id,
        expensive_func(data) AS computed
    FROM source_table
)
SELECT *
FROM expensive
UNION ALL
SELECT *
FROM expensive
WHERE computed > 100;
```

`AS MATERIALIZED` prevents recomputation. It does not provide indexes.

### 4.3 When to Use AS MATERIALIZED

There is no universal threshold.

Whether materialization helps depends on:

- Row count and width
- Computation cost
- Number of references in the query
- Available memory (work_mem)
- Query plan characteristics
- Existing indexing strategy in the original implementation

**Example: Good candidate**

```sql
WITH regional_sales AS MATERIALIZED (
    SELECT
        region,
        sum(amount) AS total
    FROM orders
    GROUP BY region
)
SELECT *
FROM regional_sales
UNION ALL
SELECT *
FROM regional_sales
WHERE total > 100000;
```

The result is reused multiple times; materialization avoids recomputation.

**Example: Poor candidate**

```sql
WITH temp_result AS MATERIALIZED (
    SELECT
        id,
        expensive_func(data) AS computed
    FROM huge_table
)
SELECT *
FROM temp_result
WHERE computed = 42;
```

If the original temp-table design relied on an index to speed the `WHERE computed = 42` lookup, a materialized CTE—which is unindexed—may perform worse.

### 4.4 Indexed Intermediate Results

A key limitation of CTEs:

**MATERIALIZED prevents recomputation. It does not provide indexes.**

Original temp-table approach:

```sql
CREATE TEMP TABLE temp_result AS
SELECT
    id,
    expensive_func(data) AS computed
FROM source_table;

CREATE INDEX ON temp_result(computed);

SELECT *
FROM temp_result
WHERE computed = 42;
```

Equivalent CTE approach:

```sql
WITH temp_result AS MATERIALIZED (
    SELECT
        id,
        expensive_func(data) AS computed
    FROM source_table
)
SELECT *
FROM temp_result
WHERE computed = 42;
```

The CTE result is unindexed and requires a full scan of the materialized result. If the original temp table used indexes, performance may degrade.

**What to do:**

- Profile with `EXPLAIN ANALYZE` on realistic data.
- Accept the performance regression if acceptable for your use case.
- Redesign the query to push predicates earlier, avoiding the need to filter the computed result.

---

## Part 5: Concurrency and Session State

### 5.1 Query-Scoped State

CTEs are query-scoped.

They:

- Create no schema objects.
- Introduce no session-state leakage.
- Are isolated across concurrent sessions.
- Disappear automatically when the query ends.

This makes them attractive replacements for many temp-table workflows.

---

### 5.2 Materialized View Refresh

#### Standard Refresh

```sql
REFRESH MATERIALIZED VIEW sales_report;
```

Acquires an `AccessExclusiveLock` on the view.

All reads are blocked during refresh.

#### Concurrent Refresh

```sql
CREATE UNIQUE INDEX sales_report_pk ON sales_report(id);

REFRESH MATERIALIZED VIEW CONCURRENTLY sales_report;
```

Allows readers to continue accessing the materialized view while refresh proceeds.

Requires:

- A suitable unique index.
- More resources (additional computation to compare old and new results).

---

## Part 6: The Missing Feature and Practical Tradeoffs

### 6.1 What PostgreSQL Lacks

Many temp-table use cases are really requesting a feature PostgreSQL does not currently provide:

```sql
DECLARE working_set TABLE (
    id int,
    value text
);
```

A function-scoped table variable would:

- Be local to a single function call.
- Avoid session-state changes.
- Avoid naming collisions.
- Eliminate explicit cleanup.

PostgreSQL does not offer this.

### 6.2 Current Alternatives

- **CTEs**: Query-scoped, no session state, works inside materialized views.
- **Recursive CTEs**: Handle hierarchies and tree traversal.
- **Arrays of composite types**: Smaller datasets, in-memory.
- **Temporary tables**: Full functionality (indexes, multiple statements) but not allowed in security-restricted operations.
- **Unlogged tables**: Faster than normal tables, but session-global and permanent; require manual cleanup.
- **Permanent staging tables**: Shared across sessions; require concurrency management.

Each has different tradeoffs.

---

## Part 7: Migration Decision Process

```
Function uses CREATE TEMP TABLE
            │
            ▼
Understand why the temp table exists
            │
 ┌──────────┼──────────┐
 │          │          │
 ▼          ▼          ▼

 Simple    Expensive   Indexed
 pipeline  reused      lookup
 
 │          │          │
 ▼          ▼          ▼

CTE     CTE AS      Redesign or
        MATERIALIZED accept perf
                    regression
```

### Rules of Thumb

1. **Simple intermediate result**: Replace with `CTE`
2. **Expensive result used multiple times**: Consider `CTE AS MATERIALIZED`; verify with `EXPLAIN ANALYZE`
3. **Intermediate result requires indexes**: CTEs are insufficient; either redesign to avoid indexing or accept performance regression

This is the most important practical consideration when converting temp-table-based code for use inside materialized-view definitions.

### Before Migrating: Profile the Original

Before deciding on a replacement strategy:

1. Determine the original function's performance characteristics.
2. Identify which temp tables were indexed and how.
3. Profile the query plan (`EXPLAIN ANALYZE`) with realistic data volumes.
4. After migration, re-profile to measure impact.

---

## References

[1] PostgreSQL 14 Documentation: CREATE MATERIALIZED VIEW  
https://www.postgresql.org/docs/14/sql-creatematerializedview.html

[2] PostgreSQL Mailing List: Discussion of security restrictions  
https://www.postgresql.org/message-id/CAFBoRzf6HwFg1jovdOrbtC6x4xKV__-t5EjSzbY2068S01pcTg%40mail.gmail.com

[3] PostgreSQL Documentation: WITH (Common Table Expressions)  
https://www.postgresql.org/docs/current/queries-with.html
