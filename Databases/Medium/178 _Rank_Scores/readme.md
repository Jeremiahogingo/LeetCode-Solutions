# 178. Rank Scores

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Database](https://img.shields.io/badge/Database-MySQL-blue)
![Topic](https://img.shields.io/badge/Topic-Window_Functions-purple)

## Problem

**LeetCode:** [178. Rank Scores](https://leetcode.com/problems/rank-scores/)

**Difficulty:** Medium

**Database:** MySQL

Given a `Scores` table containing game scores, calculate the rank of each score in descending order.

The ranking must follow these rules:

- Higher scores receive better (smaller) ranks.
- Equal scores receive the same rank.
- The next distinct score receives the next consecutive rank, without gaps.

## Table Structure

**Scores**

| Column | Type | Description |
|---|---|---|
| `id` | int | Unique score identifier |
| `score` | decimal | Game score |

## Approach: Window Functions — DENSE_RANK()

The most efficient and readable approach is to use MySQL's `DENSE_RANK()` window function.

`DENSE_RANK()` assigns the same rank to identical values and does not leave gaps between consecutive ranks.

### MySQL Solution

**File:** `178_Rank_Scores.sql`

```sql
SELECT
    score,
    DENSE_RANK() OVER (
        ORDER BY score DESC
    ) AS `rank`
FROM Scores
ORDER BY score DESC;
```

## Explanation

### 1. DENSE_RANK()

```sql
DENSE_RANK() OVER (
    ORDER BY score DESC
)
```

Calculates the dense rank of every score.

- `DENSE_RANK()` assigns consecutive ranks.
- `OVER()` defines the window over which the ranking is calculated.
- `ORDER BY score DESC` ranks scores from highest to lowest.

### 2. Column Alias

```sql
AS `rank`
```

Names the calculated column `rank`. Backticks escape the alias because `RANK` is a SQL keyword.

### 3. Final Ordering

```sql
ORDER BY score DESC;
```

Ensures that the result is displayed from the highest score to the lowest score.

## Example

### Input

**Scores**

| id | score |
|---:|---:|
| 1 | 3.50 |
| 2 | 3.65 |
| 3 | 4.00 |
| 4 | 3.85 |
| 5 | 4.00 |
| 6 | 3.65 |

### Output

| score | rank |
|---:|---:|
| 4.00 | 1 |
| 4.00 | 1 |
| 3.85 | 2 |
| 3.65 | 3 |
| 3.65 | 3 |
| 3.50 | 4 |

### Ranking Breakdown

| Score | Rank | Explanation |
|---:|---:|---|
| 4.00 | 1 | Highest score |
| 4.00 | 1 | Same score receives the same rank |
| 3.85 | 2 | Next distinct score |
| 3.65 | 3 | Next distinct score |
| 3.65 | 3 | Same score receives the same rank |
| 3.50 | 4 | Next consecutive rank |

## Understanding SQL Ranking Functions

SQL provides three commonly used ranking window functions.

Consider the scores:

`100, 100, 90, 80`

| Score | ROW_NUMBER() | RANK() | DENSE_RANK() |
|---:|---:|---:|---:|
| 100 | 1 | 1 | 1 |
| 100 | 2 | 1 | 1 |
| 90 | 3 | 3 | 2 |
| 80 | 4 | 4 | 3 |

### ROW_NUMBER()

Assigns a unique sequential number to each row, even when scores are identical.

### RANK()

Assigns the same rank to tied values but leaves gaps in subsequent rankings.

### DENSE_RANK()

Assigns the same rank to tied values without leaving gaps.

**Why DENSE_RANK()?**

The problem requires equal scores to share the same rank and subsequent ranks to remain consecutive. `DENSE_RANK()` satisfies both requirements.

## Alternative Approach: Correlated Subquery

Ranking can also be implemented without window functions by counting the number of distinct scores greater than the current score.

```sql
SELECT
    s1.score,
    (
        SELECT COUNT(DISTINCT s2.score)
        FROM Scores AS s2
        WHERE s2.score > s1.score
    ) + 1 AS `rank`
FROM Scores AS s1
ORDER BY s1.score DESC;
```

### How It Works

For each score:

1. Find all scores greater than the current score.
2. Count the distinct greater scores.
3. Add one to obtain the rank.

For example, if three distinct scores are greater than the current score, its rank is `4`.

This approach demonstrates how ranking can be derived using correlated subqueries and aggregation. However, the window-function solution is more concise and expressive.

## Complexity Analysis

Let `n` represent the number of rows in the `Scores` table.

| Metric | Complexity |
|---|---|
| Ranking and sorting | Typically `O(n log n)` |
| Correlated subquery | Up to `O(n²)` |
| Auxiliary space | Depends on the database execution plan |

The actual execution cost depends on MySQL's query optimizer, sorting strategy, and available indexes.

## Key Takeaways

1. **Window functions:** Perform calculations across related rows without collapsing the result into grouped rows.
2. **DENSE_RANK():** Assigns identical ranks to tied values without leaving gaps.
3. **RANK():** Assigns identical ranks to tied values but leaves gaps afterward.
4. **ROW_NUMBER():** Assigns a unique sequential number to every row.
5. **ORDER BY inside OVER():** Controls how ranking is calculated.
6. **Outer ORDER BY:** Controls the presentation order of the final result.
7. **Correlated subqueries:** Provide an alternative way to calculate rankings through comparisons and aggregation.

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Medium/
        └── 178_Rank_Scores.sql
```

## References

- [LeetCode 178 — Rank Scores](https://leetcode.com/problems/rank-scores/)
- [MySQL Documentation — Window Functions](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html)
- [MySQL Documentation — DENSE_RANK()](https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html#function_dense-rank)

---

**Solution Status:** Completed

**Primary Approach:** Window Functions — `DENSE_RANK()`

**Database:** MySQL

**Key Concepts:** DENSE_RANK, RANK, ROW_NUMBER, Window Functions, ORDER BY, Correlated Subqueries