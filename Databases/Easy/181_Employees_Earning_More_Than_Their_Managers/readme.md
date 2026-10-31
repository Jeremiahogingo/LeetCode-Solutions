# LeetCode 181: Employees Earning More Than Their Managers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-MySQL-blue?logo=mysql&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Self%20Join-purple)

## Problem Description

Given the `Employee` table, find the employees who earn more than their respective managers.

Each record contains an employee's ID, name, salary, and manager ID. Both employees and managers are stored in the same table.

Return the employee names under the column `Employee`.

**Problem link:** [LeetCode 181 — Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

## Approach: Self Join

Use a self join to compare each employee's salary with their manager's salary.

1. Reference the `Employee` table twice using aliases `e` and `m`.
2. Join the employee's `managerId` with the manager's `id`.
3. Compare the employee's salary against the manager's salary.
4. Return only employees earning strictly more than their managers.

The inner join automatically excludes employees without a manager.

## MySQL Solution

```sql
SELECT
    e.name AS Employee
FROM Employee AS e
JOIN Employee AS m
    ON e.managerId = m.id
WHERE e.salary > m.salary;
```

## Example

**Input: Employee**

| id | name | salary | managerId |
|---:|---|---:|---:|
| 1 | Joe | 70000 | 3 |
| 2 | Henry | 80000 | 4 |
| 3 | Sam | 60000 | NULL |
| 4 | Max | 90000 | NULL |

**Output:**

| Employee |
|---|
| Joe |

**Explanation:** Joe earns 70,000 while his manager Sam earns 60,000. Henry earns less than his manager Max, so he is excluded.

## Complexity Analysis

Let \(n\) represent the number of employee records.

- **Time Complexity:** Depends on the database execution plan and join strategy. The primary-key index on `id` supports efficient manager matching.
- **Auxiliary Space Complexity:** Depends on the join execution strategy and temporary storage requirements.

## Key Takeaways

- A self join allows a table to be compared against itself.
- Table aliases distinguish employees from managers.
- An inner join matches employees with existing managers.
- Use `>` for a strictly greater salary comparison.
- Self joins are useful for hierarchical relationships within a table.

## Related Problems

| Problem | Difficulty | Connection |
|---|---|---|
| [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | Medium | Compare and rank salary values. |
| [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) | Medium | Compare employee salaries within groups. |
| [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | Hard | Rank employees by salary within departments. |
| [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | Easy | Practice table relationships and joins. |

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Easy/
        └── 181_Employees_Earning_More_Than_Their_Managers.sql
```

## References

- [LeetCode Problem 181](https://leetcode.com/problems/employees-earning-more-than-their-managers/)
- [MySQL Documentation — JOIN](https://dev.mysql.com/doc/refman/8.4/en/join.html)
