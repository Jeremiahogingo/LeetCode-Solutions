# LeetCode 584: Find Customer Referee

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-MySQL-blue?logo=mysql&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-SQL%20Filtering-purple)

## Problem Description

Given the `Customer` table, find the names of customers who:

1. Were referred by a customer whose ID is not `2`.
2. Were not referred by anyone.

Return only the customer names. The results can be returned in any order.

**Problem link:** [LeetCode 584 — Find Customer Referee](https://leetcode.com/problems/find-customer-referee/)

## Approach: Conditional Filtering and NULL Handling

Use the `WHERE` clause with the `OR` operator to account for both conditions.

1. Use `referee_id <> 2` to select customers referred by someone other than customer `2`.
2. Use `referee_id IS NULL` to include customers without a referee.
3. Combine the conditions using `OR`.
4. Return the customer names.

An explicit `IS NULL` condition is necessary because SQL comparisons involving `NULL` evaluate to `UNKNOWN`, not `TRUE`.

## MySQL Solution

```sql
SELECT
    name
FROM Customer
WHERE referee_id <> 2
   OR referee_id IS NULL;
```

## Example

**Input: Customer**

| id | name | referee_id |
|---:|---|---:|
| 1 | Will | NULL |
| 2 | Jane | NULL |
| 3 | Alex | 2 |
| 4 | Bill | NULL |
| 5 | Zack | 1 |
| 6 | Mark | 2 |

**Output:**

| name |
|---|
| Will |
| Jane |
| Bill |
| Zack |

**Explanation:**

- Will, Jane, and Bill have no referee, so they are included.
- Zack was referred by customer `1`, so he is included.
- Alex and Mark were referred by customer `2`, so they are excluded.

## Complexity Analysis

Let \(n\) represent the number of records in the `Customer` table.

- **Time Complexity:** \(O(n)\) for evaluating the filtering conditions across the rows.
- **Auxiliary Space Complexity:** \(O(1)\) for the filtering logic, excluding database execution overhead and result storage.

## Key Takeaways

- `<>` means not equal to.
- `IS NULL` checks whether a column contains a NULL value.
- `OR` allows a record to qualify when either condition is satisfied.
- SQL uses three-valued logic: `TRUE`, `FALSE`, and `UNKNOWN`.
- Comparisons such as `referee_id = NULL` and `referee_id <> NULL` should not be used to test for missing values.
- Always consider NULL handling when filtering database records.

## Related Problems

| Problem | Difficulty | Connection |
|---|---|---|
| [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | Easy | Identify records without matching related data. |
| [595. Big Countries](https://leetcode.com/problems/big-countries/) | Easy | Apply conditional SQL filtering. |
| [1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | Easy | Combine conditions using `WHERE` and `AND`. |
| [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) | Easy | Practice filtering and relationships within database tables. |

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Easy/
        └── 584_Find_Customer_Referee.sql
```

## References

- [LeetCode Problem 584](https://leetcode.com/problems/find-customer-referee/)
- [MySQL Documentation — Working with NULL Values](https://dev.mysql.com/doc/refman/8.4/en/working-with-null.html)
- [MySQL Documentation — Comparison Operators](https://dev.mysql.com/doc/refman/8.4/en/comparison-operators.html)
