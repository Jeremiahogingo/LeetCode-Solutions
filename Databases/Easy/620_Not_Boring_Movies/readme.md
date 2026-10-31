# LeetCode 620: Not Boring Movies

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-MySQL-blue?logo=mysql&logoColor=white)
![Topics](https://img.shields.io/badge/Topics-Filtering%20%7C%20Sorting-purple)

## Problem Description

Given the `Cinema` table, find movies that satisfy both conditions:

- Have an odd-numbered ID.
- Have a description that is not equal to `"boring"`.

Return all columns and order the results by rating in descending order.

**Problem link:** [LeetCode 620 — Not Boring Movies](https://leetcode.com/problems/not-boring-movies/)

## Approach: Filtering and Sorting

Use the `WHERE` clause to select qualifying movies and `ORDER BY` to sort the results.

1. Use the modulo operator `%` to identify odd-numbered IDs.
2. Use `<>` to exclude movies described as `"boring"`.
3. Combine both conditions using `AND`.
4. Sort the selected movies by `rating` in descending order.

## MySQL Solution

```sql
SELECT
    id,
    movie,
    description,
    rating
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
```

## Example

**Input: Cinema**

| id | movie | description | rating |
|---:|---|---|---:|
| 1 | War | great 3D | 8.9 |
| 2 | Science | fiction | 8.5 |
| 3 | irish | boring | 6.2 |
| 4 | Ice song | Fantacy | 8.6 |
| 5 | House card | Interesting | 9.1 |

**Output:**

| id | movie | description | rating |
|---:|---|---|---:|
| 5 | House card | Interesting | 9.1 |
| 1 | War | great 3D | 8.9 |

**Explanation:**

The odd-numbered IDs are `1`, `3`, and `5`. Movie `3` is excluded because its description is `"boring"`.

The remaining movies are sorted by rating from highest to lowest.

## Complexity Analysis

Let \(n\) represent the number of records in the `Cinema` table.

- **Time Complexity:** Typically \(O(n \log n)\) when sorting the qualifying results. The actual cost depends on the database execution plan and available indexes.
- **Auxiliary Space Complexity:** Depends on the database sorting strategy and temporary storage requirements.

## Key Takeaways

- `%` is the modulo operator and can identify odd or even numbers.
- `<>` represents the not-equal comparison operator.
- `WHERE` filters records using specified conditions.
- `AND` requires multiple conditions to be satisfied.
- `ORDER BY ... DESC` sorts values from highest to lowest.

## Related Problems

| Problem | Difficulty | Connection |
|---|---|---|
| [595. Big Countries](https://leetcode.com/problems/big-countries/) | Easy | Filter records using multiple conditions. |
| [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | Easy | Apply conditional filtering with SQL. |
| [1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | Easy | Filter rows using multiple criteria. |
| [1148. Article Views I](https://leetcode.com/problems/article-views-i/) | Easy | Filter records and return selected columns. |

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Easy/
        └── 620_Not_Boring_Movies.sql
```

## References

- [LeetCode Problem 620](https://leetcode.com/problems/not-boring-movies/)
- [MySQL Documentation — Operators](https://dev.mysql.com/doc/refman/8.4/en/non-typed-operators.html)
- [MySQL Documentation — SELECT](https://dev.mysql.com/doc/refman/8.4/en/select.html)
