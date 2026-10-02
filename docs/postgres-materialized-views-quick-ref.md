# PostgreSQL: Materialized Views and Temp Tables

## Quick Reference

**Problem:** PostgreSQL forbids `CREATE TEMP TABLE` inside materialized-view definitions.

**Reason:** Temp tables modify session state. Materialized views execute in security-restricted mode to prevent unpredictable behavior.

**Solution:** Replace temp tables with **CTEs** (Common Table Expressions).

---

## When to Use CTEs

| Use Case | Approach | Notes |
|----------|----------|-------|
| Simple pipeline (2–3 steps) | Basic `WITH` clause | No session state, automatically cleaned up |
| Expensive result used multiple times | `WITH ... AS MATERIALIZED` | Prevents recomputation; profile with `EXPLAIN ANALYZE` |
| Intermediate result needs indexes | Redesign query or accept perf regression | CTEs are unindexed; this is a hard limitation |
| Hierarchical data (trees, graphs) | `WITH RECURSIVE` | Preferred over multiple temp tables |

---

## Basic Example

**Before (fails in materialized views):**
```sql
CREATE FUNCTION process_data()
RETURNS TABLE (id INT, result TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    CREATE TEMP TABLE step1 AS
    SELECT id, data FROM source_table;
    
    CREATE INDEX ON step1(id);
    
    SELECT id, upper(data) FROM step1;
END;
$$;
```

**After (works in materialized views):**
```sql
CREATE FUNCTION process_data()
RETURNS TABLE (id INT, result TEXT)
LANGUAGE SQL
STABLE
AS $$
WITH step1 AS (
    SELECT id, data FROM source_table
)
SELECT id, upper(data) AS result FROM step1;
$$;
```

---

## Key Differences

| Feature | Temp Table | CTE |
|---------|-----------|-----|
| Session state | Modifies (`pg_temp`) | None (query-scoped) |
| In materialized views | ❌ Forbidden | ✅ Allowed |
| Indexes | ✅ Supported | ❌ Not supported |
| Multiple statements | ✅ Full plpgsql | ❌ SQL-only (usually) |
| Cleanup | Manual | Automatic |

---

## Common Pitfalls

**1. Assuming VOLATILE functions are forbidden**

Not true. Materialized views forbid *temp-table creation*, not VOLATILE functions generally.

```sql
-- This works (no temp table created):
CREATE MATERIALIZED VIEW mv AS
SELECT some_volatile_function();
```

**2. Using AS MATERIALIZED for unindexed filters**

If your original temp-table query relied on indexes, `AS MATERIALIZED` won't help:

```sql
-- Original: had an index on computed
CREATE TEMP TABLE t AS SELECT id, expensive_func(data) AS computed FROM huge_table;
CREATE INDEX ON t(computed);
SELECT * FROM t WHERE computed = 42;

-- CTE version: unindexed, full scan of computed result
WITH t AS MATERIALIZED (
    SELECT id, expensive_func(data) AS computed FROM huge_table
)
SELECT * FROM t WHERE computed = 42;
```

Profile with `EXPLAIN ANALYZE` before and after.

**3. Overusing WITH RECURSIVE**

Use only when the CTE actually references itself (for hierarchies, traversals). Simple pipelines don't need `RECURSIVE`.

```sql
-- Unnecessary RECURSIVE:
WITH RECURSIVE simple AS (
    SELECT id, data FROM table1
)
SELECT * FROM simple;

-- Correct:
WITH simple AS (
    SELECT id, data FROM table1
)
SELECT * FROM simple;
```

---

## Decision Tree

```
Need a temp table in a materialized-view context?
            ↓
    ┌───────┴───────┐
    ↓               ↓
Simple result?   Complex needs?
    ↓               ↓
   CTE          ┌────┴────┐
                ↓         ↓
           Reused?    Indexed
           multiple   lookup?
           times?      ↓
            ↓        ❌ Redesign
        ✅ CTE AS   or accept
        MATERIALIZED  regression
```

---

## See Also

- [Full Reference: Temp Tables, Materialized Views, CTEs, and Security-Restricted Operations](./postgres-temp-tables-materialized-views.md) — Detailed guidance on volatility, CTE inlining, concurrency, and migration strategies.
- [PostgreSQL Docs: Common Table Expressions](https://www.postgresql.org/docs/current/queries-with.html)
- [PostgreSQL Docs: CREATE MATERIALIZED VIEW](https://www.postgresql.org/docs/14/sql-creatematerializedview.html)
