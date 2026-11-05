# LeetCode 586: Customer Placing the Largest Number of Orders

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-MySQL-blue?logo=mysql&logoColor=white)
![Topics](https://img.shields.io/badge/Topics-GROUP%20BY%20%7C%20Aggregation%20%7C%20Sorting-purple)

## Problem Description

Given the `Orders` table, find the `customer_number` of the customer who has placed the largest number of orders.

Each row represents an order and the customer who placed it.

The problem guarantees that exactly one customer has placed more orders than every other customer.

**Problem link:** [LeetCode 586 — Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/)

## Approach: GROUP BY, COUNT(), and ORDER BY

Use SQL aggregation to count the orders placed by each customer, then sort the results to identify the customer with the highest order count.

1. Group all records by `customer_number`.
2. Use `COUNT(*)` to calculate the number of orders per customer.
3. Sort the grouped results by order count in descending order.
4. Use `LIMIT 1` to return the customer with the highest order count.

## MySQL Solution

```sql
SELECT
    customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
```

## Example

**Input: Orders**

| order_number | customer_number |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 3 |

**Output:**

| customer_number |
|---:|
| 3 |

**Explanation:**

After grouping and counting:

| customer_number | order_count |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |

Customer `3` has placed two orders, while customers `1` and `2` have each placed one order.

Therefore, customer `3` has the largest number of orders.

## Follow-up: Handling Ties

What happens if multiple customers have the same maximum number of orders?

Instead of using `LIMIT 1`, use `HAVING` with a subquery to return every customer whose order count equals the maximum count.

```sql
SELECT
    customer_number
FROM Orders
GROUP BY customer_number
HAVING COUNT(*) = (
    SELECT MAX(order_count)
    FROM (
        SELECT COUNT(*) AS order_count
        FROM Orders
        GROUP BY customer_number
    ) AS customer_orders
);
```

This version returns all customers tied for the highest number of orders.

## Complexity Analysis

Let \(n\) represent the number of records in the `Orders` table.

- **Time Complexity:** Typically \(O(n\log n)\) when sorting the grouped customer counts. Actual performance depends on the database execution plan.
- **Auxiliary Space Complexity:** Depends on the grouping and sorting strategy and the number of distinct customers.

## Key Takeaways

- `GROUP BY` creates a group for each customer.
- `COUNT(*)` calculates the number of orders in each group.
- `ORDER BY ... DESC` ranks customers by their order frequency.
- `LIMIT 1` retrieves the highest-ranked customer.
- `HAVING` filters grouped results using aggregate conditions.
- When ties are possible, compare each group's count against the maximum rather than limiting the result to one row.

## Related Problems

These problems reinforce SQL aggregation, filtering, ranking, and grouping techniques.

| Problem | Difficulty | Connection |
|---|---|---|
| [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) | Easy | Group records and identify repeated values. |
| [511. Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | Easy | Group records and apply aggregate functions. |
| [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | Easy | Apply conditional filtering to customer records. |
| [586. Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) | Easy | Group customers and rank them by order count. |
| [178. Rank Scores](https://leetcode.com/problems/rank-scores/) | Medium | Rank grouped values using SQL. |
| [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | Hard | Apply ranking and aggregation within groups. |

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Easy/
        └── 586_Customer_Placing_the_Largest_Number_of_Orders/
            ├── solution.sql
            └── README.md
```

## References

- [LeetCode Problem 586](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/)
- [MySQL Documentation — Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)
- [MySQL Documentation — GROUP BY](https://dev.mysql.com/doc/refman/8.4/en/group-by-handling.html)
- [MySQL Documentation — SELECT and LIMIT](https://dev.mysql.com/doc/refman/8.4/en/select.html)