# PostgreSQL: Materialized Views and Temp Tables

## At a Glance

✅ CTE (`WITH`)
- Query-scoped
- No session state changes
- Works in materialized views

✅ CTE AS MATERIALIZED
- Prevents recomputation
- Still not indexed

⚠️ Temp tables with indexes
- Often hardest to migrate
- May require query redesign

❌ Function-local table variables
- Not currently available in PostgreSQL

---

## Quick Reference

**Problem:** Functions used by `CREATE MATERIALIZED VIEW` or `REFRESH MATERIALIZED VIEW` cannot create temporary tables.

**Reason:** Materialized-view queries execute in a security-restricted context. Creating a temporary table would modify session state.

**Solution:** Most temp-table pipelines can be rewritten as CTEs (`WITH` clauses). Some indexed temp-table workloads may require redesign.

---

## When to Use CTEs

| Use Case | Recommended Approach | Notes |
|----------|---------------------|-------|
| Simple intermediate result | `WITH` | Query-scoped, no session state |
| Expensive computation reused multiple times | `WITH ... AS MATERIALIZED` | Prevents recomputation; verify with `EXPLAIN ANALYZE` |
| Hierarchy/tree traversal | `WITH RECURSIVE` | Only when actual recursion exists |
| Need indexes on intermediate result | Redesign or accept regression | CTEs do not create indexes |

---

## Basic Example

```sql
CREATE OR REPLACE FUNCTION process_data()
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
)
SELECT
    id,
    upper(data) AS result
FROM step1;
$$;

CREATE MATERIALIZED VIEW mv AS
SELECT *
FROM process_data();
```

---

## Recursive Example

```sql
CREATE OR REPLACE FUNCTION hierarchy_walk()
RETURNS TABLE (
    id INT,
    parent_id INT,
    depth INT
)
LANGUAGE SQL
STABLE
AS $$
WITH RECURSIVE hierarchy AS (
    SELECT
        id,
        parent_id,
        1 AS depth
    FROM nodes
    WHERE parent_id IS NULL

    UNION ALL

    SELECT
        child.id,
        child.parent_id,
        parent.depth + 1
    FROM nodes child
    JOIN hierarchy parent
      ON child.parent_id = parent.id
)
SELECT *
FROM hierarchy;
$$;
```

Use `WITH RECURSIVE` only when a CTE references itself.

---

## Important Clarifications

### Materialized Views Do Not Ban VOLATILE Functions

Incorrect:

> Materialized views forbid VOLATILE functions.

Correct:

> Materialized views forbid operations such as temporary-table creation within their security-restricted execution context.

A VOLATILE function may still work if it does not perform restricted operations.

---

### SQL-Language Functions Are Not Read-Only

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

**Note:** SQL-language functions execute a single SQL statement. If you need variables, loops, exception handling, or multiple statements, use PL/pgSQL.

---

## CTE Materialization

### Force Materialization

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

### What MATERIALIZED Does

✅ Stores the intermediate result once

✅ Prevents recomputation

❌ Does not create indexes

❌ Does not create a reusable table

---

## Indexed Intermediate Results

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

CTE replacement:

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

The CTE result is unindexed. Performance may be worse if the original design relied on indexes.

Temp tables provide two capabilities:

1. Persistence across multiple statements
2. Indexes on intermediate results

CTEs fully replace neither capability. Indexed temp-table workloads are often the hardest to migrate.

---

## Concurrency

CTEs are query-scoped:

- No schema objects created
- No session-state leakage
- Safe across concurrent sessions
- Automatically cleaned up

---

## Materialized View Refresh

### Standard Refresh

```sql
REFRESH MATERIALIZED VIEW sales_report;
```

- Blocks readers during refresh
- Simpler execution

### Concurrent Refresh

```sql
CREATE UNIQUE INDEX sales_report_pk
ON sales_report(id);

REFRESH MATERIALIZED VIEW CONCURRENTLY sales_report;
```

- Allows continued reads
- Requires a suitable unique index
- Uses additional resources

---

## Choosing an Intermediate Result Mechanism

| Requirement | Recommended Tool |
|-------------|------------------|
| Single-query pipeline | CTE |
| Recursive traversal | Recursive CTE |
| Reused expensive subquery | CTE AS MATERIALIZED |
| Indexed intermediate result | Temp table |
| Security-restricted operation | CTE |
| Session-local scratch space | Temp table |
| Materialized view definition | CTE |
| Function-local table variable | Not available in PostgreSQL |
| Shared staging area | Unlogged or permanent table |

---

## Decision Flow

```text
Need a temp table in a materialized-view context?
        |
        v
Simple intermediate data?
        |
   yes -> use CTE
        |
   no -> expensive and reused?
        |
   yes -> consider AS MATERIALIZED
        |
        v
Does the result need indexes?
        |
   yes -> redesign or accept regression
   no -> CTE / CTE AS MATERIALIZED
```

---

## Migration Checklist

1. Identify why each temp table exists.
2. Determine whether indexes are used.
3. Replace simple pipelines with CTEs.
4. Consider `AS MATERIALIZED` for expensive reused results.
5. Benchmark with `EXPLAIN ANALYZE`.
6. Re-profile after migration using realistic data volumes.
7. Review indexed intermediate-result workloads separately.

---

## Key Takeaway

For materialized-view-compatible code:

- Use CTEs for most intermediate-result pipelines.
- Use `AS MATERIALIZED` when avoiding recomputation matters.
- Recognize that indexed temp-table workflows may require redesign.
- Understand that PostgreSQL currently has no true function-scoped table variables.
- Treat the restriction as a session-state/security constraint, not a blanket prohibition on VOLATILE functions.

---

## See Also

- [Full Reference: Temp Tables, Materialized Views, CTEs, and Security-Restricted Operations](./postgres-temp-tables-materialized-views.md)
- [PostgreSQL Docs: WITH (Common Table Expressions)](https://www.postgresql.org/docs/current/queries-with.html)
- [PostgreSQL Docs: CREATE MATERIALIZED VIEW](https://www.postgresql.org/docs/14/sql-creatematerializedview.html)
