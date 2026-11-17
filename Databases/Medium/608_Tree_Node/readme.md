# 608. Tree Node

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-MySQL-blue)
![Topic](https://img.shields.io/badge/Topic-Database%20%7C%20CASE%20%7C%20Subqueries-informational)

## Problem

**[Tree Node](https://leetcode.com/problems/tree-node/)**

Given a table named `Tree` containing two columns:

- `id`: The unique identifier of a node.
- `p_id`: The identifier of the node's parent. If the node has no parent, `p_id` is `NULL`.

Classify each node in the tree according to the following rules:

- **Root:** The node has no parent.
- **Leaf:** The node has a parent but has no children.
- **Inner:** The node has a parent and at least one child.

Return the `id` of each node and its corresponding `type`.

---

## Approach: CASE Expression + Subquery

The solution uses a `CASE` expression to classify nodes based on their parent-child relationships.

### Classification logic

1. **Root:** If `p_id IS NULL`, the node is the root.
2. **Inner:** If the node's `id` appears in the `p_id` column, another node references it as its parent. Therefore, it has at least one child.
3. **Leaf:** If neither condition applies, the node has no children and is not the root.

The root condition must be checked first because a root node can also have children.

---

## MySQL Solution

**File:** `608_Tree_Node.sql`

```sql
SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (
            SELECT p_id
            FROM Tree
            WHERE p_id IS NOT NULL
        ) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;
```

---

## Example

### Input

**Tree table**

| id | p_id |
|---:|---:|
| 1 | NULL |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 2 |

### Output

| id | type |
|---:|---|
| 1 | Root |
| 2 | Inner |
| 3 | Leaf |
| 4 | Leaf |
| 5 | Leaf |

### Explanation

- Node `1` is the root because it has no parent.
- Node `2` is an inner node because its parent is `1` and it has children `4` and `5`.
- Node `3` is a leaf because it has a parent but no children.
- Nodes `4` and `5` are leaves because neither has children.

---

## Complexity Analysis

Let `n` represent the number of rows in the `Tree` table.

- **Time Complexity:** Depends on MySQL's execution plan and available indexes. The query examines the nodes and checks whether each node is referenced as a parent.
- **Space Complexity:** Depends on how MySQL executes the subquery and whether it uses an internal structure for membership testing.

---

## Key Takeaways

- `CASE WHEN` is useful for classifying records based on multiple conditions.
- `IS NULL` identifies nodes without parents.
- `IN` with a subquery checks whether a value exists in another result set.
- Parent-child relationships can be analyzed using a single table through self-referencing identifiers.
- Condition ordering matters when multiple classification rules may apply.

## Repository Structure

```text
LeetCode-Solutions/
└── Databases/
    └── Medium/
        ├── 608_Tree_Node.sql
        └── README.md
```

## References

- [LeetCode Problem 608 — Tree Node](https://leetcode.com/problems/tree-node/)
- [MySQL CASE Expression](https://dev.mysql.com/doc/refman/8.4/en/flow-control-functions.html)
- [MySQL Subqueries](https://dev.mysql.com/doc/refman/8.4/en/subqueries.html)

---

**Author:** [Jeremiah Ogingo](https://github.com/Jeremiahogingo)

**Repository:** [LeetCode-Solutions](https://github.com/Jeremiahogingo/LeetCode-Solutions)