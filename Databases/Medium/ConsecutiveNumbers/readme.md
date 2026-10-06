# 🔢 Consecutive Numbers

![LeetCode](https://img.shields.io/badge/LeetCode-180-orange?style=flat-square\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=flat-square)
![Language](https://img.shields.io/badge/Language-SQL-blue?style=flat-square)

## 📌 Overview

Find all numbers that appear **at least three times consecutively** in the `Logs` table.

The rows are ordered using the `id` column.

## 🧠 Approach

Use the SQL `LAG()` window function to compare each number with the previous two rows.

A number is consecutive when:

```text
Current = Previous = Two rows before
```

`DISTINCT` ensures each qualifying number appears only once.

## 💻 SQL Query

```sql
SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM Logs
) t
WHERE num = prev_num
  AND num = prev_prev_num;
```

## 🔍 Example

Input:

```text
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
```

Output:

```text
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
```

## ⚠️ Edge Cases

| Case                               | Behavior                |
| ---------------------------------- | ----------------------- |
| Three identical numbers            | Number is returned      |
| More than three consecutive values | Number is returned once |
| Two identical values               | Not returned            |
| No consecutive values              | Empty result            |
| Multiple qualifying numbers        | Each appears once       |

## ⏱️ Complexity

* **Time:** `O(n)` conceptually, depending on the database's window-function execution.
* **Space:** Depends on the database's window-function implementation.

## 💡 Key Takeaway

`LAG()` is useful for comparing a row with previous rows. For this problem, checking the current value against the previous two values identifies three consecutive occurrences.

## 📖 Reference

[LeetCode — Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/)
