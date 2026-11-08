# 1267. Count Servers that Communicate

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topic](https://img.shields.io/badge/Topic-Matrix%20%7C%20Counting-purple)
![LeetCode](https://img.shields.io/badge/LeetCode-1267-yellow)

## Problem

**[Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/description/)**

You are given an `m x n` binary matrix `grid`, where:

- `1` represents a server.
- `0` represents an empty cell.

Two servers can communicate if they are located in the same row or the same column.

Return the number of servers that can communicate with at least one other server.

## Approach: Row and Column Frequency Counting

The solution uses two passes through the matrix and two auxiliary arrays to count the number of servers in each row and column.

### Algorithm

1. Initialize `row_count` to store the number of servers in each row.
2. Initialize `col_count` to store the number of servers in each column.
3. Traverse the matrix and increment the corresponding row and column counts whenever a server is encountered.
4. Traverse the matrix again.
5. Count a server if its row contains more than one server **or** its column contains more than one server.
6. Return the total count.

The logical `OR` is important: a server only needs another server in either its row or its column to communicate.

## Solution

```python
from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_count = [0] * m
        col_count = [0] * n

        # Count servers in each row and column.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Count servers that can communicate.
        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        result += 1

        return result
```

## Examples

### Example 1

**Input:**
```python
grid = [[1, 0], [0, 1]]
```

**Output:**
```python
0
```

**Explanation:**

Both servers are isolated. They share neither a row nor a column with another server.

### Example 2

**Input:**
```python
grid = [[1, 0], [1, 1]]
```

**Output:**
```python
3
```

**Explanation:**

All three servers can communicate:

- The first-column servers communicate with each other.
- The two servers in the second row communicate with each other.

### Example 3

**Input:**
```python
grid = [
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
```

**Output:**
```python
4
```

**Explanation:**

The two servers in the first row communicate, as do the two servers in the third column. The remaining server is isolated.

## Complexity Analysis

Let `m` represent the number of rows and `n` represent the number of columns.

| Complexity | Analysis |
|---|---|
| Time | `O(m × n)` |
| Auxiliary Space | `O(m + n)` |

**Time Complexity: `O(m × n)`**

- The first traversal counts servers in every row and column.
- The second traversal checks whether each server can communicate.
- Each cell is visited twice, resulting in linear time relative to the matrix size.

**Space Complexity: `O(m + n)`**

Two auxiliary arrays are used: one of size `m` and another of size `n`.

## Key Takeaways

- Row and column frequency counting can simplify matrix-based problems.
- Precomputation avoids repeatedly scanning entire rows and columns.
- A server communicates when either its row count or column count exceeds one.
- Two linear traversals are sufficient to solve the problem efficiently.

## Related Problems

- [LeetCode 1971 – Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)
- [LeetCode 2352 – Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/)
- [LeetCode 1582 – Special Positions in a Binary Matrix](https://leetcode.com/problems/special-positions-in-a-binary-matrix/)

## Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── Python/
        ├── 1267_Count_Servers_that_Communicate.py
        └── README.md
```

## References

- [LeetCode Problem – Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/)
- [NeetCode – Problem Explanation](https://neetcode.io/solutions/count-servers-that-communicate)

---

**Problem:** 1267  
**Difficulty:** Medium  
**Language:** Python  
**Topics:** Array, Matrix, Counting