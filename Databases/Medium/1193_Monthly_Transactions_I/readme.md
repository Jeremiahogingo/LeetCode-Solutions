# 1193. Monthly Transactions I

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-MySQL-blue)
![Category](https://img.shields.io/badge/Category-Database-purple)
![Topic](https://img.shields.io/badge/Topic-Aggregation%20%7C%20Filtering-green)

## Problem

**[Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/description/)**

Given a `Transactions` table, calculate monthly transaction statistics grouped by month and country.

For each month-country combination, return:

- `month`: Transaction month in `YYYY-MM` format.
- `country`: Transaction country.
- `trans_count`: Total number of transactions.
- `approved_count`: Number of approved transactions.
- `trans_total_amount`: Total amount of all transactions.
- `approved_total_amount`: Total amount of approved transactions.

## Database Schema

**Table: Transactions**

| Column | Type |
|---|---|
| id | int |
| country | varchar |
| state | enum |
| amount | int |
| trans_date | date |

The `state` column contains transaction statuses such as `approved` and `declined`.

## Approach: Grouping and Conditional Aggregation

The solution uses SQL aggregation functions alongside conditional expressions to calculate the required statistics.

### Algorithm

1. Use `DATE_FORMAT()` to extract the year and month from `trans_date`.
2. Group transactions by the formatted month and country.
3. Use `COUNT(*)` to calculate the total number of transactions.
4. Use `SUM(CASE WHEN ...)` to count approved transactions.
5. Use `SUM(amount)` to calculate the total transaction amount.
6. Use conditional aggregation to calculate the total amount of approved transactions.

## SQL Solution

```sql
SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY
    DATE_FORMAT(trans_date, '%Y-%m'),
    country;
```

## Example

**Input: Transactions**

| id | country | state | amount | trans_date |
|---:|---|---|---:|---|
| 121 | US | approved | 1000 | 2018-12-18 |
| 122 | US | declined | 2000 | 2018-12-19 |
| 123 | US | approved | 2000 | 2019-01-01 |
| 124 | DE | approved | 2000 | 2019-01-07 |

**Output:**

| month | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
|---|---|---:|---:|---:|---:|
| 2018-12 | US | 2 | 1 | 3000 | 1000 |
| 2019-01 | US | 1 | 1 | 2000 | 2000 |
| 2019-01 | DE | 1 | 1 | 2000 | 2000 |

**Explanation:**

- December 2018, US: Two transactions occurred, one approved. Their combined amount is 3000, while the approved amount is 1000.
- January 2019, US: One transaction occurred and was approved, totaling 2000.
- January 2019, DE: One transaction occurred and was approved, totaling 2000.

## Complexity Analysis

Let `N` represent the number of rows in the `Transactions` table.

| Complexity | Analysis |
|---|---|
| Time | Depends on the database execution plan and grouping strategy; typically O(N) for scanning and aggregating the records, excluding sorting overhead. |
| Space | Depends on the number of distinct month-country groups maintained by the database. |

The database must process the transaction records and maintain aggregate values for each group.

## Key Takeaways

- `DATE_FORMAT()` extracts and formats date components.
- `COUNT(*)` counts all records in a group.
- `SUM()` calculates aggregate totals.
- `CASE WHEN` enables conditional aggregation.
- `GROUP BY` supports aggregation across multiple columns.
- Conditional aggregation can calculate several related statistics in one query.

## Related Problems

- [LeetCode 586 – Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/)
- [LeetCode 596 – Classes With at Least 5 Students](https://leetcode.com/problems/classes-with-at-least-5-students/)
- [LeetCode 1174 – Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/)

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Medium/
        ├── 1193_Monthly_Transactions_I.sql
        └── README.md
```

## References

- [LeetCode – Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/)
- [MySQL Documentation – Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)
- [MySQL Documentation – Date and Time Functions](https://dev.mysql.com/doc/refman/8.4/en/date-and-time-functions.html)

---

**Problem:** 1193  
**Difficulty:** Medium  
**Language:** MySQL  
**Topics:** Database, SQL, Grouping, Aggregation, Conditional Expressions