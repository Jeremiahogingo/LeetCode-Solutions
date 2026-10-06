# 🔗 Combine Two Tables

![LeetCode](https://img.shields.io/badge/LeetCode-175-orange?style=flat-square\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Language-SQL-blue?style=flat-square)

## 📌 Overview

Combine the `Person` and `Address` tables to display each person's:

* `firstName`
* `lastName`
* `city`
* `state`

Every person must appear in the result, even if they do not have an address.

## 🧠 Approach

Use a **LEFT JOIN** between `Person` and `Address` using `personId`.

* `Person` is the main table.
* `Address` provides the city and state.
* If no matching address exists, `city` and `state` are returned as `NULL`.

## 💻 SQL Query

```sql
SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
    ON p.personId = a.personId;
```

## 🔍 Example

```text
Person                         Address
+----------+--------+-------+  +----------+-----------+
| personId | lastName| firstName| personId | city      |
+----------+--------+-------+  +----------+-----------+
| 1        | Wang   | Allen |  | 2        | New York  |
| 2        | Alice  | Bob   |  +----------+-----------+
+----------+--------+-------+
```

Result:

```text
+-----------+----------+----------+-------+
| firstName | lastName | city     | state |
+-----------+----------+----------+-------+
| Allen     | Wang     | NULL     | NULL  |
| Bob       | Alice    | New York | NY    |
+-----------+----------+----------+-------+
```

## ⚠️ Edge Cases

| Case                  | Behavior                      |
| --------------------- | ----------------------------- |
| Person has an address | Address details are included  |
| Person has no address | `city` and `state` are `NULL` |
| Empty `Address` table | All people are still returned |
| Empty `Person` table  | No rows are returned          |

## ⏱️ Complexity

* **Time:** `O(P + A)` typically with an efficient join strategy
* **Space:** Depends on the database's join implementation

## 💡 Key Takeaway

Use **LEFT JOIN** when all records from the first table must be preserved, even when there is no matching record in the second table.


## 📖 Reference

[LeetCode — Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)
