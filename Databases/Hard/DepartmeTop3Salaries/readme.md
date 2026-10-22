# 185. Department Top Three Salaries

![LeetCode](https://img.shields.io/badge/LeetCode-185-orange?logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Language](https://img.shields.io/badge/Language-MySQL-blue?logo=mysql)
![Topic](https://img.shields.io/badge/Topic-Window%20Functions-success)

## Problem Overview

Given the `Employee` and `Department` tables, find employees whose salaries belong to the **top three distinct salary levels within their respective departments**.

Employees with equal salaries must receive the same rank, and all employees whose salaries qualify must be returned. A department with fewer than three distinct salaries should return all its employees.

**LeetCode:** [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description/)

## Approach: DENSE_RANK()

The solution uses the SQL window function `DENSE_RANK()` to rank employee salaries independently within each department.

### Algorithm

1. Use `DENSE_RANK()` to rank employees by salary in descending order.
2. Use `PARTITION BY departmentId` to restart the ranking for each department.
3. Join the ranked employees with `Department` to retrieve department names.
4. Filter the results to include only ranks less than or equal to `3`.

### Why DENSE_RANK()?

`DENSE_RANK()` assigns the same rank to equal salaries without skipping subsequent ranks.

For example:

| Salary | DENSE_RANK() | RANK() |
|---:|---:|---:|
| 90000 | 1 | 1 |
| 85000 | 2 | 2 |
| 85000 | 2 | 2 |
| 70000 | 3 | 4 |
| 69000 | 4 | 5 |

The requirement concerns the top three **distinct salary values**, not exactly three employees. Therefore, `DENSE_RANK()` is the appropriate function.

## MySQL Implementation

```sql
WITH RankedEmployees AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM Employee e
    JOIN Department d
        ON e.departmentId = d.id
)
SELECT
    Department,
    Employee,
    Salary
FROM RankedEmployees
WHERE salary_rank <= 3;
```

## Example Walkthrough

### Input

**Employee**

| id | name | salary | departmentId |
|---:|---|---:|---:|
| 1 | Joe | 85000 | 1 |
| 2 | Henry | 80000 | 2 |
| 3 | Sam | 60000 | 2 |
| 4 | Max | 90000 | 1 |
| 5 | Janet | 69000 | 1 |
| 6 | Randy | 85000 | 1 |
| 7 | Will | 70000 | 1 |

**Department**

| id | name |
|---:|---|
| 1 | IT |
| 2 | Sales |

### Ranking Results

Within the IT department:

| Employee | Salary | Rank |
|---|---:|---:|
| Max | 90000 | 1 |
| Joe | 85000 | 2 |
| Randy | 85000 | 2 |
| Will | 70000 | 3 |
| Janet | 69000 | 4 |

Within the Sales department:

| Employee | Salary | Rank |
|---|---:|---:|
| Henry | 80000 | 1 |
| Sam | 60000 | 2 |

Filtering with `salary_rank <= 3` includes Max, Joe, Randy, Will, Henry, and Sam. Janet is excluded because her salary ranks fourth in IT.

### Expected Output

| Department | Employee | Salary |
|---|---|---:|
| IT | Max | 90000 |
| IT | Joe | 85000 |
| IT | Randy | 85000 |
| IT | Will | 70000 |
| Sales | Henry | 80000 |
| Sales | Sam | 60000 |

The output order is not guaranteed because the problem permits results in any order.

## Edge Cases

| Scenario | Expected Behavior |
|---|---|
| Employees have identical salaries | All tied employees receive the same rank and are included if that rank is at most 3 |
| Department has one distinct salary | All employees in that department qualify |
| Department has two distinct salaries | Employees earning either salary qualify |
| Department has three distinct salaries | Employees earning all three salary levels qualify |
| Department has more than three distinct salaries | Employees ranked fourth or lower are excluded |
| Different departments have overlapping salary values | Each department is ranked independently |
| More than three employees qualify due to ties | All qualifying employees are returned |

## Complexity Analysis

Let \(N\) be the number of employees.

- **Time Complexity:** Typically \(O(N \log N)\), due to sorting for window-function ranking, depending on the database execution plan.
- **Space Complexity:** Up to \(O(N)\) for intermediate ranking and sorting operations, depending on the database execution plan.

These are typical estimates rather than guarantees; actual costs depend on the database engine and its execution plan.

## Key Takeaways

- Use `DENSE_RANK()` when ranking distinct values while preserving ties.
- `PARTITION BY` creates independent ranking groups.
- `ORDER BY salary DESC` places the highest salary first.
- Filtering the computed rank in an outer query or CTE makes the ranking logic clear.
- Always distinguish between the top three employees and employees earning the top three distinct salaries.

## Related Problems

- [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)
- [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)
- [178. Rank Scores](https://leetcode.com/problems/rank-scores/)

## References

- [LeetCode #185 — Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description/)
- [MySQL Documentation — Window Functions](https://dev.mysql.com/doc/refman/8.4/en/window-functions.html)

---

*Part of my [LeetCode Solutions](https://github.com/Jeremiahogingo/LeetCode-Solutions) repository.*