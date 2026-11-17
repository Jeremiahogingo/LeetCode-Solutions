# 1341. Movie Rating

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-MySQL-blue)
![Topic](https://img.shields.io/badge/Topic-Database%20%7C%20Aggregation-informational)

## Problem

**[Movie Rating](https://leetcode.com/problems/movie-rating/)**

You are given three tables:

- `Movies`: Contains movie IDs and titles.
- `Users`: Contains user IDs and names.
- `MovieRating`: Contains movie ratings, user IDs, and rating dates.

Write a solution to:

1. Find the name of the user who has rated the greatest number of movies. If multiple users have rated the same number of movies, return the lexicographically smallest name.
2. Find the movie with the highest average rating during February 2020. If multiple movies have the same average rating, return the lexicographically smallest title.

Return the results in a single column named `results`, containing exactly two rows.

---

## Approach: Aggregation + Sorting + UNION ALL

The solution uses two independent queries and combines their results with `UNION ALL`.

### 1. Find the user with the most ratings

- Join `Users` and `MovieRating` using `user_id`.
- Group the records by user.
- Use `COUNT(*)` to calculate the number of ratings submitted by each user.
- Sort by rating count in descending order.
- Use the user's name in ascending order to resolve ties.
- Return the first result using `LIMIT 1`.

### 2. Find the highest-rated movie in February 2020

- Join `Movies` and `MovieRating` using `movie_id`.
- Filter ratings to February 2020.
- Group records by movie.
- Calculate each movie's average rating using `AVG()`.
- Sort by average rating in descending order.
- Sort by movie title in ascending order to resolve ties.
- Return the first result using `LIMIT 1`.

### 3. Combine both results

Use `UNION ALL` to combine the two queries into the required two-row result.

---

## MySQL Solution

**File:** `1341_Movie_Rating.sql`

```sql id="x8czk3"
(
    SELECT
        u.name AS results
    FROM Users u
    JOIN MovieRating mr
        ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name ASC
    LIMIT 1
)

UNION ALL

(
    SELECT
        m.title AS results
    FROM Movies m
    JOIN MovieRating mr
        ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01'
      AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
);
```

---

## Example

### Input

**Users**

| user_id | name |
|---:|---|
| 1 | Daniel |
| 2 | Monica |
| 3 | Maria |

**Movies**

| movie_id | title |
|---:|---|
| 1 | Avengers |
| 2 | Frozen 2 |
| 3 | Joker |

**MovieRating**

| movie_id | user_id | rating | created_at |
|---:|---:|---:|---|
| 1 | 1 | 3 | 2020-01-12 |
| 1 | 2 | 4 | 2020-02-11 |
| 1 | 3 | 2 | 2020-02-12 |
| 2 | 1 | 5 | 2020-02-17 |
| 2 | 2 | 5 | 2020-02-20 |
| 3 | 1 | 2 | 2020-02-18 |
| 3 | 2 | 3 | 2020-02-19 |

### Output

| results |
|---|
| Daniel |
| Frozen 2 |

### Explanation

**User ranking:**

- Daniel and Monica each rated three movies.
- Maria rated fewer movies.
- Daniel is selected because his name comes first alphabetically.

**Movie ranking:**

- Frozen 2 has an average February rating of `5.0`.
- Joker has an average February rating of `2.5`.
- Frozen 2 has the highest average rating.

---

## Complexity Analysis

Let:

- `U` be the number of users.
- `M` be the number of movies.
- `R` be the number of movie-rating records.

The query performs two aggregations over rating records.

- **Time Complexity:** Approximately `O(R log R)` as a general sorting-based upper-level estimate, depending on the database execution plan and indexes.
- **Space Complexity:** Depends on MySQL's grouping, sorting, and temporary-table execution strategy.

The actual execution cost is determined by the database optimizer, available indexes, and table sizes.

---

## Key Takeaways

- `COUNT(*)` counts the number of ratings submitted by each user.
- `AVG()` calculates the average rating for each movie.
- `GROUP BY` performs aggregation at the user or movie level.
- `ORDER BY` supports ranking and alphabetical tie-breaking.
- `LIMIT 1` selects the highest-ranked record.
- `UNION ALL` combines independent query results without removing duplicates.
- Using an inclusive start date and exclusive end date correctly filters the entire month of February, including timestamps.

## Repository Structure

```text id="v7z4lq"
LeetCode-Solutions/
└── Databases/
    └── Medium/
        ├── 608_Tree_Node.sql
        ├── 1341_Movie_Rating.sql
        └── README.md
```

## References

- [LeetCode Problem 1341 — Movie Rating](https://leetcode.com/problems/movie-rating/)
- [MySQL Aggregate Functions](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)
- [MySQL UNION Clause](https://dev.mysql.com/doc/refman/8.4/en/union.html)
- [MySQL SELECT Statement](https://dev.mysql.com/doc/refman/8.4/en/select.html)

---

**Author:** [Jeremiah Ogingo](https://github.com/Jeremiahogingo)

**Repository:** [LeetCode-Solutions](https://github.com/Jeremiahogingo/LeetCode-Solutions)