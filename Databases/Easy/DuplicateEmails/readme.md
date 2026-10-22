# 182. Duplicate Emails

![LeetCode](https://img.shields.io/badge/LeetCode-182-orange?logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-MySQL-blue?logo=mysql)
![Topic](https://img.shields.io/badge/Topic-Aggregation-success)

## Problem Overview

Given the `Person` table, identify all email addresses that appear more than once.

Each row contains a unique `id` and an `email`. The result must contain each duplicated email only once, and the output can be returned in any order.

**LeetCode:** [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/description/)

## Approach: GROUP BY + HAVING

Duplicate detection is a counting problem. We group rows by email, count the rows in each group, and keep only groups whose count exceeds one.

### Algorithm

1. Read the records from the `Person` table.
2. Group rows by `email` using `GROUP BY`.
3. Count the rows in each group using `COUNT(*)`.
4. Filter groups with `HAVING COUNT(*) > 1`.
5. Return the duplicated email addresses under the required column name, `Email`.

### Why HAVING Instead of WHERE?

- `WHERE` filters individual rows before grouping.
- `HAVING` filters groups after aggregation.

Because the condition depends on `COUNT(*)`, `HAVING` is the appropriate clause.

## MySQL Implementation

```sql
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```

## Example Walkthrough

### Input

**Person**

| id | email |
|---:|---|
| 1 | a@b.com |
| 2 | c@d.com |
| 3 | a@b.com |
| 4 | d@e.com |
| 5 | d@e.com |

### Grouping and Counting

| Email | Occurrences | Result |
|---|---:|---|
| a@b.com | 2 | Include |
| c@d.com | 1 | Exclude |
| d@e.com | 2 | Include |

The query groups identical addresses together and returns only those appearing more than once.

### Expected Output

| Email |
|---|
| a@b.com |
| d@e.com |

The output order is not guaranteed because the problem accepts results in any order.

## Edge Cases

| Scenario | Expected Behavior |
|---|---|
| Every email is unique | Returns an empty result |
| An email appears exactly twice | Returns that email once |
| An email appears three or more times | Still returns that email once |
| Multiple emails are duplicated | Returns every duplicated email |
| The table contains one row | Returns an empty result |
| No rows are present | Returns an empty result |

The problem guarantees that `email` is not `NULL`, so no special null handling is required.

## Complexity Analysis

Let \(n\) be the number of rows in `Person` and \(k\) the number of distinct email addresses.

- **Time Complexity:** Typically \(O(n \log n)\) when sorting is used for grouping; hash-based aggregation may have \(O(n)\) average behavior.
- **Space Complexity:** Up to \(O(k)\) for the aggregation state, depending on the database execution plan.

Actual performance depends on the database engine, indexes, and execution plan.

## Key Takeaways

- `GROUP BY` combines rows with identical values.
- `COUNT(*)` counts the rows in each group.
- `HAVING COUNT(*) > 1` identifies duplicates.
- Grouping naturally returns each duplicated email once.
- Use `HAVING` when filtering depends on an aggregate function.

## Related Problems

- [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/)
- [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)
- [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)

## References

- [LeetCode #182 — Duplicate Emails](https://leetcode.com/problems/duplicate-emails/description/)
- [MySQL Documentation — Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)

---

*Part of my [LeetCode Solutions](https://github.com/Jeremiahogingo/LeetCode-Solutions) repository.*