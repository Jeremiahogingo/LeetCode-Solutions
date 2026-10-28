# LeetCode 62: Unique Paths

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topic](https://img.shields.io/badge/Topic-Dynamic%20Programming-purple)

## Problem Description

A robot is located at the top-left corner of an `m × n` grid and needs to reach the bottom-right corner.

The robot can only move **right** or **down** at any point. Given `m` and `n`, return the total number of unique paths the robot can take to reach the destination.

**Problem link:** [LeetCode 62 — Unique Paths](https://leetcode.com/problems/unique-paths/description/)

## Approach: Space-Optimized Dynamic Programming

Each cell can be reached from either the cell above or the cell to its left. Therefore, the number of paths to a cell is the sum of the paths to those two neighboring cells.

Instead of storing the entire grid in a two-dimensional DP table, use a one-dimensional array.

1. Initialize every entry in `dp` to `1`, since there is only one way to reach any cell in the first row.
2. Iterate through the remaining rows and columns.
3. Update each entry by adding the number of paths from the left to the existing number of paths from above.
4. Return the last entry, which contains the total number of paths to the destination.

## Python Solution

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]
```

## Examples

**Example 1**

- Input: `m = 3, n = 7`
- Output: `28`

**Example 2**

- Input: `m = 3, n = 2`
- Output: `3`
- Explanation: The three possible paths are Right → Down → Down, Down → Right → Down, and Down → Down → Right.

**Example 3**

- Input: `m = 1, n = 1`
- Output: `1`
- Explanation: The robot is already at the destination.

## Complexity Analysis

Let \(m\) be the number of rows and \(n\) be the number of columns.

- **Time Complexity:** \(O(mn)\) — each DP state is updated in constant time.
- **Auxiliary Space Complexity:** \(O(n)\) — only one array of length \(n\) is maintained.

## Key Takeaways

- Dynamic programming avoids recomputing the same subproblems.
- The number of paths to a cell depends on the paths to the cell above and the cell to the left.
- Space optimization is possible when each state only needs previously computed values.
- Grid path-counting problems often use similar DP transitions.

## Related Problems

These problems build on similar dynamic programming and grid-traversal concepts.

| Problem | Difficulty | Connection |
|---|---|---|
| [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | Medium | Count paths while avoiding obstacles. |
| [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Medium | Find the minimum-cost path through a grid. |
| [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | Count possible ways to reach a destination using DP. |
| [120. Triangle](https://leetcode.com/problems/triangle/) | Medium | Optimize a path through a triangular structure. |
| [174. Dungeon Game](https://leetcode.com/problems/dungeon-game/) | Hard | Use dynamic programming to find the minimum initial health needed to reach a destination. |

## Repository Structure

```text
Unique_Paths/
├── solution.py
└── README.md
```

## References

- [LeetCode Problem 62](https://leetcode.com/problems/unique-paths/description/)
- [NeetCode — Unique Paths Explanation](https://neetcode.io/solutions/unique-paths)
- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
