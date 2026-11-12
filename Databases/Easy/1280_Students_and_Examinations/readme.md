# 1280. Students and Examinations

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Language](https://img.shields.io/badge/Language-MySQL-blue)
![Category](https://img.shields.io/badge/Category-Database-purple)
![Topic](https://img.shields.io/badge/Topic-Joins%20%7C%20Aggregation-green)
![LeetCode](https://img.shields.io/badge/LeetCode-1280-orange)

## Problem

**[Students and Examinations](https://leetcode.com/problems/students-and-examinations/)**

Given three database tables, `Students`, `Subjects`, and `Examinations`, calculate how many times each student attended an examination for every available subject.

The result must include:

- Every student.
- Every subject for each student.
- The number of examination attendances for each student-subject combination.
- Combinations with no examination attendance, represented by `0`.

The final result must be ordered by `student_id` and `subject_name`.

## Database Schema

### 1. Students

| Column | Type |
|---|---|
| student_id | int |
| student_name | varchar |

Contains student identification numbers and names.

### 2. Subjects

| Column | Type |
|---|---|
| subject_name | varchar |

Contains all available examination subjects.

### 3. Examinations

| Column | Type |
|---|---|
| student_id | int |
| subject_name | varchar |

Each row represents one examination attendance by a student for a particular subject.

**Important:** Duplicate examination records represent separate attendances and must be counted individually.

## Approach: CROSS JOIN + LEFT JOIN + GROUP BY

The main challenge is ensuring that every student-subject combination appears in the result, including combinations where a student has never attended an examination.

The solution combines three SQL operations.

### 1. CROSS JOIN — Generate All Combinations

```sql
FROM Students s
CROSS JOIN Subjects sub
```

A `CROSS JOIN` generates every possible combination between students and subjects.

For example, if there are:

- 4 students.
- 3 subjects.

The resulting intermediate table contains:

\[
4 \times 3 = 12 \text{ combinations}
\]

This guarantees that every student is paired with every available subject.

### 2. LEFT JOIN — Match Examination Records

```sql
LEFT JOIN Examinations e
    ON s.student_id = e.student_id
    AND sub.subject_name = e.subject_name
```

The `LEFT JOIN` connects each student-subject combination with its matching examination records.

We use `LEFT JOIN` rather than `INNER JOIN` because students who have not attended an examination must still appear in the result.

When no matching examination exists, the columns from `Examinations` contain `NULL`.

### 3. COUNT() — Calculate Attendance

```sql
COUNT(e.student_id) AS attended_exams
```

`COUNT(column)` counts only non-NULL values.

Therefore:

- Matching examination records are counted.
- Missing examination records are ignored.
- A combination without examinations correctly receives a count of `0`.

We use `COUNT(e.student_id)` instead of `COUNT(*)` because `COUNT(*)` would also count the unmatched row produced by the `LEFT JOIN`.

### 4. GROUP BY — Aggregate Results

```sql
GROUP BY
    s.student_id,
    s.student_name,
    sub.subject_name
```

This groups examination records by student and subject, allowing us to calculate the total attendance for every combination.

### 5. ORDER BY — Sort the Results

```sql
ORDER BY
    s.student_id,
    sub.subject_name;
```

Sorts the output by student ID, followed by subject name.

## SQL Solution

```sql
SELECT
    s.student_id,
    s.student_name,
    sub.subject_name,
    COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
    ON s.student_id = e.student_id
    AND sub.subject_name = e.subject_name
GROUP BY
    s.student_id,
    s.student_name,
    sub.subject_name
ORDER BY
    s.student_id,
    sub.subject_name;
```

## Example

### Input

**Students**

| student_id | student_name |
|---:|---|
| 1 | Alice |
| 2 | Bob |
| 13 | John |
| 6 | Alex |

**Subjects**

| subject_name |
|---|
| Math |
| Physics |
| Programming |

**Examinations**

| student_id | subject_name |
|---:|---|
| 1 | Math |
| 1 | Math |
| 1 | Math |
| 1 | Physics |
| 1 | Physics |
| 1 | Programming |
| 2 | Math |
| 2 | Programming |
| 13 | Math |
| 13 | Physics |
| 13 | Programming |

### Output

| student_id | student_name | subject_name | attended_exams |
|---:|---|---|---:|
| 1 | Alice | Math | 3 |
| 1 | Alice | Physics | 2 |
| 1 | Alice | Programming | 1 |
| 2 | Bob | Math | 1 |
| 2 | Bob | Physics | 0 |
| 2 | Bob | Programming | 1 |
| 6 | Alex | Math | 0 |
| 6 | Alex | Physics | 0 |
| 6 | Alex | Programming | 0 |
| 13 | John | Math | 1 |
| 13 | John | Physics | 1 |
| 13 | John | Programming | 1 |

### Explanation

The `CROSS JOIN` first produces all 12 student-subject combinations.

The `LEFT JOIN` then attaches matching examination records.

For example:

| Student | Subject | Attendance |
|---|---|---:|
| Alice | Math | 3 |
| Alice | Physics | 2 |
| Alice | Programming | 1 |
| Bob | Math | 1 |
| Bob | Physics | 0 |
| Bob | Programming | 1 |
| Alex | Math | 0 |

The `COUNT(e.student_id)` expression counts matching records while ignoring NULL values.

Consequently, students without examination attendance are included with a count of `0`.

## Complexity Analysis

Let:

- `S` represent the number of students.
- `U` represent the number of subjects.
- `E` represent the number of examination records.

| Operation | Size / Cost |
|---|---|
| CROSS JOIN | Produces `S × U` combinations |
| LEFT JOIN | Matches examination records to combinations |
| GROUP BY | Aggregates results by student and subject |
| ORDER BY | Sorts the final result |

**Intermediate Result Size:**

\[
O(S \times U)
\]

The Cartesian product produces one row for every student-subject combination before examination records are matched.

The actual execution time and memory usage depend on the database execution plan, available indexes, join strategy, and sorting or grouping implementation.

The required output itself contains exactly `S × U` rows.

## Important Concepts

| SQL Concept | Purpose |
|---|---|
| `CROSS JOIN` | Generates all possible student-subject combinations |
| `LEFT JOIN` | Preserves combinations without matching examination records |
| `COUNT(column)` | Counts non-NULL matching records |
| `GROUP BY` | Aggregates attendance by student and subject |
| `ORDER BY` | Sorts the final output |

## Common Mistakes

### 1. Using INNER JOIN Instead of LEFT JOIN

An `INNER JOIN` excludes student-subject combinations without matching examination records.

**Solution:** Use `LEFT JOIN` to preserve all combinations.

### 2. Forgetting the CROSS JOIN

Joining only `Students` and `Examinations` would exclude students and subjects without attendance records.

**Solution:** Generate all possible combinations using `CROSS JOIN` first.

### 3. Using COUNT(*)

```sql
COUNT(*)
```

This counts the unmatched row created by a `LEFT JOIN`, potentially returning `1` instead of `0`.

**Solution:**

```sql
COUNT(e.student_id)
```

This ignores NULL values from unmatched examination records.

### 4. Using COUNT(DISTINCT ...)

Distinct counting would remove duplicate attendance records.

**Solution:** Use ordinary `COUNT()` because every examination record represents a separate attendance.

### 5. Forgetting ORDER BY

The problem requires results ordered by student ID and subject name.

**Solution:**

```sql
ORDER BY s.student_id, sub.subject_name;
```

## Key Takeaways

- `CROSS JOIN` is useful when every possible combination of two datasets is required.
- `LEFT JOIN` preserves unmatched records from the left-side result.
- `COUNT(column)` ignores NULL values, making it useful for counting matching records after an outer join.
- `COUNT(*)` and `COUNT(column)` can produce different results when NULL values are involved.
- Duplicate records must be preserved when each row represents a separate event.
- Combining joins with aggregation is a fundamental SQL technique for reporting and analytics.

## Related Problems

| Problem | Difficulty | Main Concept |
|---|---|---|
| [1193. Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/) | Medium | Conditional Aggregation |
| [1141. User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) | Easy | Date Filtering and Aggregation |
| [586. Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) | Easy | GROUP BY |
| [596. Classes With at Least 5 Students](https://leetcode.com/problems/classes-with-at-least-5-students/) | Easy | GROUP BY and HAVING |

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Easy/
        ├── 1280_Students_and_Examinations.sql
        └── README.md
```

## References

- [LeetCode – Students and Examinations](https://leetcode.com/problems/students-and-examinations/)
- [MySQL Documentation – JOIN Clause](https://dev.mysql.com/doc/refman/8.4/en/join.html)
- [MySQL Documentation – Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)

---

**Problem:** 1280

**Difficulty:** Easy

**Language:** MySQL

**Topics:** Database, CROSS JOIN, LEFT JOIN, GROUP BY, COUNT, Aggregation

**Key Technique:** Generate all combinations, preserve unmatched records, then aggregate attendance.