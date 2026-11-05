# LeetCode 596: Classes With at Least 5 Students

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-MySQL-blue?logo=mysql&logoColor=white)
![Topics](https://img.shields.io/badge/Topics-GROUP%20BY%20%7C%20Aggregation-purple)

## Problem Description

Given the `Courses` table, find all classes that have at least five students enrolled.

Each row represents a student's enrollment in a particular class. The combination of `student` and `class` is the primary key, ensuring that a student cannot be counted more than once in the same class.

Return the class names in any order.

**Problem link:** [LeetCode 596 — Classes With at Least 5 Students](https://leetcode.com/problems/classes-with-at-least-5-students/description/)

## Approach: GROUP BY and HAVING

Use SQL aggregation to count the students enrolled in each class, then filter groups containing at least five students.

1. Group enrollment records by `class`.
2. Use `COUNT(*)` to count the students in each class.
3. Apply `HAVING COUNT(*) >= 5` to retain classes with at least five students.
4. Return the qualifying class names.

`HAVING` is necessary because the filtering condition depends on an aggregate calculation.

## MySQL Solution

```sql
SELECT
    class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
```

## Example

**Input: Courses**

| student | class |
|---|---|
| A | Math |
| B | English |
| C | Math |
| D | Biology |
| E | Math |
| F | Computer |
| G | Math |
| H | Math |
| I | Math |

**Output:**

| class |
|---|
| Math |

**Explanation:**

After grouping and counting:

| class | Student count |
|---|---:|
| Math | 6 |
| English | 1 |
| Biology | 1 |
| Computer | 1 |

Only Math has at least five students, so it is the only class returned.

## Complexity Analysis

Let \(n\) represent the number of enrollment records and \(c\) the number of distinct classes.

- **Time Complexity:** Typically \(O(n)\) with hash-based aggregation; sorting-based execution may require \(O(n\log n)\).
- **Auxiliary Space Complexity:** Typically \(O(c)\) for storing grouped aggregation data, depending on the database execution plan.

## Key Takeaways

- `GROUP BY` organizes records into groups based on a column.
- `COUNT(*)` counts the records in each group.
- `HAVING` filters groups after aggregation.
- `WHERE` filters individual rows before aggregation.
- The composite primary key `(student, class)` guarantees that counting rows gives the number of distinct students per class.

## Related Problems

These problems reinforce SQL grouping, aggregation, filtering, and counting.

| Problem | Difficulty | Connection |
|---|---|---|
| [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) | Easy | Group records and identify repeated values. |
| [511. Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | Easy | Group records and apply aggregate functions. |
| [586. Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) | Easy | Count records per group and identify the highest count. |
| [1729. Find Followers Count](https://leetcode.com/problems/find-followers-count/) | Easy | Count records associated with each user. |
| [178. Rank Scores](https://leetcode.com/problems/rank-scores/) | Medium | Rank values using SQL aggregation and window-style logic. |

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Easy/
        └── 596_Classes_With_At_Least_5_Students/
            ├── solution.sql
            └── README.md
```

## References

- [LeetCode Problem 596](https://leetcode.com/problems/classes-with-at-least-5-students/description/)
- [MySQL Documentation — Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)
- [MySQL Documentation — GROUP BY and HAVING](https://dev.mysql.com/doc/refman/8.4/en/group-by-handling.html)
