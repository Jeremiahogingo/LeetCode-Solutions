# LeetCode 511: Game Play Analysis I

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-MySQL-blue?logo=mysql&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-SQL%20Aggregation-purple)

## Problem Description

Given the `Activity` table, write a SQL query to find the **first login date for each player**.

Each record represents a player's activity on a particular date, including the device used and the number of games played.

Return the result with two columns: `player_id` and `first_login`.

**Problem link:** [LeetCode 511 — Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/description/)

## Approach: GROUP BY and MIN()

Use SQL aggregation to find the earliest login date for every player.

1. Group records using `player_id`.
2. Apply `MIN(event_date)` to find the earliest date in each player's group.
3. Rename the aggregated column to `first_login`.
4. Return the player ID alongside the earliest login date.

## MySQL Solution

```sql
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
```

## Example

**Input: Activity**

| player_id | device_id | event_date | games_played |
|---:|---:|---|---:|
| 1 | 2 | 2016-03-01 | 5 |
| 1 | 2 | 2016-05-02 | 6 |
| 2 | 3 | 2017-06-25 | 1 |
| 3 | 1 | 2016-03-02 | 0 |
| 3 | 4 | 2018-07-03 | 5 |

**Output:**

| player_id | first_login |
|---:|---|
| 1 | 2016-03-01 |
| 2 | 2017-06-25 |
| 3 | 2016-03-02 |

**Explanation:** `MIN(event_date)` selects the earliest login date for each player, even when a player has multiple activity records.

## Complexity Analysis

Let \(n\) represent the number of rows in the `Activity` table.

- **Time Complexity:** Typically \(O(n)\) for hash-based aggregation; sorting-based execution may require \(O(n\log n)\).
- **Space Complexity:** Depends on the database execution plan and the number of distinct players being grouped.

## Key Takeaways

- `GROUP BY` combines rows sharing the same player ID.
- `MIN()` retrieves the earliest date within each group.
- Aggregate functions simplify queries involving grouped records.
- `AS` provides a meaningful alias for the resulting column.
- The query does not require sorting the final result because LeetCode accepts any order.

## Related Problems

These problems provide additional practice with SQL aggregation and game activity analysis.

| Problem | Difficulty | Connection |
|---|---|---|
| [512. Game Play Analysis II](https://leetcode.com/problems/game-play-analysis-ii/) | Easy | Find the device used during each player's first login. |
| [534. Game Play Analysis III](https://leetcode.com/problems/game-play-analysis-iii/) | Medium | Calculate cumulative games played over time for each player. |
| [550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/) | Medium | Analyze consecutive login activity using dates and player groups. |

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Easy/
        └── 511_Game_Play_Analysis_I.sql
```

## References

- [LeetCode Problem 511](https://leetcode.com/problems/game-play-analysis-i/description/)
- [MySQL Documentation — Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)
- [MySQL Documentation — GROUP BY](https://dev.mysql.com/doc/refman/8.4/en/group-by-handling.html)
