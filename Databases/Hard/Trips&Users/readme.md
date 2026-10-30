# LeetCode 262: Trips and Users

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)
![Language](https://img.shields.io/badge/Language-MySQL-blue?logo=mysql&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-JOINs%20%7C%20Aggregation-purple)

## Problem Description

Given the `Trips` and `Users` tables, calculate the daily cancellation rate of taxi requests between **October 1, 2013 and October 3, 2013**.

A trip should only be included when **both the client and the driver are not banned**.

The cancellation rate is calculated as:

\[
\text{Cancellation Rate} =
\frac{\text{Number of cancelled trips}}
{\text{Total valid trips}}
\]

The result must be rounded to two decimal places.

**Problem link:** [LeetCode 262 — Trips and Users](https://leetcode.com/problems/trips-and-users/)

## Approach: Multiple JOINs and Conditional Aggregation

Use the `Users` table twice to independently verify the client's and driver's banned status, then group valid trips by date.

1. **Join clients:** Match `Trips.client_id` with `Users.users_id` and retain only unbanned clients.
2. **Join drivers:** Join `Users` again using `driver_id` and retain only unbanned drivers.
3. **Filter dates:** Include requests from October 1 through October 3, 2013.
4. **Calculate cancellations:** Use `AVG(status != 'completed')` to treat cancelled trips as `1` and completed trips as `0`.
5. **Group by date:** Calculate a separate cancellation rate for each day.
6. **Round the result:** Use `ROUND()` to return two decimal places.

## MySQL Solution

```sql
SELECT
    t.request_at AS Day,
    ROUND(AVG(t.status != 'completed'), 2) AS `Cancellation Rate`
FROM Trips AS t
JOIN Users AS c
    ON t.client_id = c.users_id
    AND c.banned = 'No'
JOIN Users AS d
    ON t.driver_id = d.users_id
    AND d.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;
```

## Examples

**Example 1**

Input: `Trips` and `Users` tables containing trip requests and user information.

Output:

| Day | Cancellation Rate |
|---|---:|
| 2013-10-01 | 0.33 |
| 2013-10-02 | 0.00 |
| 2013-10-03 | 0.50 |

**Explanation:**

- **October 1:** Three valid trips remain after excluding requests involving banned users. One was cancelled, giving a rate of `1/3 = 0.33`.
- **October 2:** Two valid trips remain, and neither was cancelled. The rate is `0.00`.
- **October 3:** Two valid trips remain, and one was cancelled. The rate is `0.50`.

## Complexity Analysis

Let \(T\) represent the number of trip records and \(U\) the number of user records.

- **Time Complexity:** Depends on the database execution plan, join strategy, indexes, and grouping operations.
- **Space Complexity:** Depends on the temporary storage required for joins and aggregation.

## Key Takeaways

- `JOIN` connects related records across tables.
- Joining the same table twice with different aliases allows independent verification of clients and drivers.
- Filtering both users is essential to exclude invalid trips.
- `AVG()` can calculate a cancellation ratio using Boolean expressions in MySQL.
- `GROUP BY` calculates separate statistics for each date.
- `ROUND()` controls the precision of the final result.

## Related Problems

These problems reinforce SQL joins, aggregation, filtering, and analytical queries.

| Problem | Difficulty | Connection |
|---|---|---|
| [511. Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | Easy | Group records by player and calculate the earliest login date. |
| [550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/) | Medium | Analyze user activity using joins and date-based calculations. |
| [1193. Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/) | Medium | Calculate totals and conditional counts using aggregation. |
| [1174. Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/) | Medium | Calculate a percentage using conditional aggregation. |
| [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | Hard | Apply more advanced SQL techniques to grouped data. |

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Hard/
        └── 262_Trips_and_Users.sql
```

## References

- [LeetCode Problem 262](https://leetcode.com/problems/trips-and-users/)
- [MySQL Documentation — JOIN](https://dev.mysql.com/doc/refman/8.4/en/join.html)
- [MySQL Documentation — Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)
- [MySQL Documentation — GROUP BY](https://dev.mysql.com/doc/refman/8.4/en/group-by-handling.html)
