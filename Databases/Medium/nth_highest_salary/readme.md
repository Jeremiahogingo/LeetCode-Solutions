# LeetCode 177: Nth Highest Salary

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-MySQL-blue)
![Topic](https://img.shields.io/badge/Topic-Database-purple)

## Problem Description

Write a MySQL function that returns the \(N\)-th highest **distinct salary** from the `Employee` table.

If fewer than \(N\) distinct salaries exist, the function must return `NULL`.

**Problem link:** [LeetCode 177 — Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/description/)

## Approach: DISTINCT, Sorting, and LIMIT

Use `DISTINCT` to remove duplicate salaries, sort the remaining values in descending order, and use `LIMIT` to retrieve the salary at the required position.

1. Decrease `N` by one because SQL's `LIMIT` offset starts at zero.
2. Retrieve distinct salaries from `Employee`.
3. Sort salaries from highest to lowest.
4. Skip the first `N` salaries and return the next one.
5. If the requested position does not exist, the scalar subquery returns `NULL`.

## MySQL Solution

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;

    RETURN (
        SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT N, 1
    );
END
```

## Examples

**Example 1**

Input:

| Id | Salary |
|---:|---:|
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |

`N = 2`

Output:

| getNthHighestSalary(2) |
|---:|
| 200 |

Explanation: The distinct salaries in descending order are `300`, `200`, and `100`. The second-highest salary is `200`.

**Example 2**

Input:

| Id | Salary |
|---:|---:|
| 1 | 100 |

`N = 2`

Output:

| getNthHighestSalary(2) |
|---|
| NULL |

Explanation: Only one distinct salary exists, so there is no second-highest salary.

**Example 3 — Duplicate salaries**

Input:

| Id | Salary |
|---:|---:|
| 1 | 300 |
| 2 | 300 |
| 3 | 200 |
| 4 | 100 |

`N = 2`

Output: `200`

Explanation: Duplicate salaries count only once when determining the rank.

## Complexity Analysis

Let \(n\) be the number of rows in the `Employee` table.

- **Time Complexity:** Typically \(O(n \log n)\) when the database must sort the distinct salaries. The actual execution cost depends on the query plan and available indexes.
- **Space Complexity:** Depends on the execution plan, including temporary storage used for duplicate elimination and sorting.

## Key Takeaways

- `DISTINCT` ensures duplicate salaries do not affect ranking.
- `ORDER BY Salary DESC` places the highest salary first.
- `LIMIT offset, count` selects rows starting at a zero-based offset.
- If the requested salary does not exist, the function returns `NULL`.
- The same pattern can be adapted to retrieve other ranked values from database tables.

## Related Problems

These problems reinforce salary ranking, ordering, and SQL window functions.

| Problem | Difficulty | Connection |
|---|---|---|
| [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | Medium | Find the second-highest distinct salary. |
| [178. Rank Scores](https://leetcode.com/problems/rank-scores/) | Medium | Rank values using SQL window functions. |
| [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) | Medium | Use SQL to identify patterns across ordered rows. |
| [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) | Medium | Find the highest salary within each department. |
| [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | Hard | Find the top three distinct salaries per department. |

## Repository Structure

```text
Nth_Highest_Salary/
├── solution.sql
└── README.md
```

## References

- [LeetCode Problem 177](https://leetcode.com/problems/nth-highest-salary/description/)
- [MySQL Documentation — SELECT](https://dev.mysql.com/doc/refman/8.4/en/select.html)
- [MySQL Documentation — LIMIT](https://dev.mysql.com/doc/refman/8.4/en/select.html#select-limit)
