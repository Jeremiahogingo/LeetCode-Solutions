# 1141. User Activity for the Past 30 Days I

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-MySQL-blue)
![Category](https://img.shields.io/badge/Category-Database-purple)
![Topic](https://img.shields.io/badge/Topic-Date%20Filtering%20%7C%20Aggregation-green)

## Problem

**[User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/)**

Given an `Activity` table, find the daily number of active users during the 30-day period ending on **2019-07-27**, inclusive.

A user is considered active on a day if they performed at least one activity on that date.

Return the activity date as `day` and the number of distinct active users as `active_users`.

## Database Schema

**Table: Activity**

| Column | Type |
|---|---|
| user_id | int |
| session_id | int |
| activity_date | date |
| activity_type | enum |

The `activity_type` column contains activity types such as `open_session`, `end_session`, `scroll_down`, and `send_message`.

## Approach: Date Filtering and Aggregation

The solution uses `WHERE`, `COUNT(DISTINCT ...)`, and `GROUP BY` to calculate the number of unique active users per day.

### Algorithm

1. Filter activity records to include dates from `2019-06-28` through `2019-07-27`.
2. Group the remaining records by `activity_date`.
3. Use `COUNT(DISTINCT user_id)` to count each user only once per day.
4. Rename `activity_date` to `day`.
5. Return the daily active user counts.

**Important:** The date range is inclusive, covering exactly 30 calendar days.

## SQL Solution

```sql
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date;
```

## Example

**Input: Activity**

| user_id | session_id | activity_date | activity_type |
|---:|---:|---|---|
| 1 | 1 | 2019-07-20 | open_session |
| 1 | 1 | 2019-07-20 | scroll_down |
| 2 | 2 | 2019-07-21 | send_message |
| 3 | 3 | 2019-07-21 | open_session |
| 1 | 4 | 2019-06-28 | end_session |
| 4 | 5 | 2019-06-25 | open_session |

**Output:**

| day | active_users |
|---|---:|
| 2019-06-28 | 1 |
| 2019-07-20 | 1 |
| 2019-07-21 | 2 |

**Explanation:**

- On `2019-07-20`, user 1 performed two activities but is counted only once.
- On `2019-07-21`, users 2 and 3 were active, giving a count of 2.
- On `2019-06-28`, user 1 was active.
- The activity on `2019-06-25` is excluded because it falls outside the specified period.

Only dates with recorded activity appear in the result.

## Complexity Analysis

Let `N` represent the number of records in the `Activity` table.

| Complexity | Analysis |
|---|---|
| Time | Depends on the execution plan, indexes, and grouping strategy; typically O(N) for scanning and aggregation, excluding sorting overhead. |
| Space | Depends on the number of distinct activity dates and the database's aggregation strategy. |

The database processes the relevant activity records and maintains distinct user counts for each date.

## Key Takeaways

- `BETWEEN` filters records within an inclusive date range.
- `COUNT(DISTINCT user_id)` prevents duplicate user counting.
- `GROUP BY` aggregates activity records by date.
- `AS` assigns meaningful column aliases.
- Multiple activities by one user on the same date should count as one active user.

## Related Problems

- [LeetCode 1193 – Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/)
- [LeetCode 550 – Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/)
- [LeetCode 586 – Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/)

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Easy/
        ├── 1141_User_Activity_for_the_Past_30_Days_I.sql
        └── README.md
```

## References

- [LeetCode – User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/)
- [MySQL Documentation – Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)
- [MySQL Documentation – Comparison Operators](https://dev.mysql.com/doc/refman/8.4/en/comparison-operators.html)

---

**Problem:** 1141  
**Difficulty:** Easy  
**Language:** MySQL  
**Topics:** Database, Date Filtering, Aggregation, Grouping, Distinct Counting