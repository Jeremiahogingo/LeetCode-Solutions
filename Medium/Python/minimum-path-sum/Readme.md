# 🛣️ 64. Minimum Path Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Topics](https://img.shields.io/badge/Topics-Dynamic%20Programming%20%7C%20Matrix-blue)
![Language](https://img.shields.io/badge/Python-3776AB?style=flat\&logo=python\&logoColor=white)

## 📖 Overview

This problem asks us to determine the **minimum possible sum** of values collected while traveling from the **top-left** corner of a grid to the **bottom-right** corner.

Movement is restricted to only two directions:

* ➡️ Right
* ⬇️ Down

Since each decision depends on previously computed results, this is a classic **Dynamic Programming (DP)** problem.

---

# 💡 Core Idea

Every cell can only be reached from:

* the cell directly above it, or
* the cell directly to its left.

Therefore, the minimum cost to reach a cell is simply:

```text
Current Cell Value + min(Top Cell, Left Cell)
```

Instead of exploring every possible path (which would be exponential), Dynamic Programming stores the best result for every cell and builds the solution incrementally.

---

# 🧠 Dynamic Programming State

Let:

```text
dp[r][c]
```

represent the minimum path sum required to reach cell `(r, c)`.

Transition:

```text
dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
```

Instead of allocating a separate DP table, we reuse the original grid to store these values, reducing the extra memory usage to **O(1)**.

---

# ⚙️ Algorithm

1. Update the first row since it can only be reached from the left.
2. Update the first column since it can only be be reached from above.
3. Traverse the remaining cells.
4. For each cell:

   * Choose the smaller of the top and left path sums.
   * Add the current cell value.
5. Return the value stored in the bottom-right corner.

---

# 🐍 Python Solution

```python
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        for c in range(1, cols):
            grid[0][c] += grid[0][c - 1]

        for r in range(1, rows):
            grid[r][0] += grid[r - 1][0]

        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[-1][-1]
```

---

# ☕ Java Solution

```java
class Solution {

    public int minPathSum(int[][] grid) {

        int rows = grid.length;
        int cols = grid[0].length;

        for (int c = 1; c < cols; c++) {
            grid[0][c] += grid[0][c - 1];
        }

        for (int r = 1; r < rows; r++) {
            grid[r][0] += grid[r - 1][0];
        }

        for (int r = 1; r < rows; r++) {
            for (int c = 1; c < cols; c++) {
                grid[r][c] += Math.min(grid[r - 1][c], grid[r][c - 1]);
            }
        }

        return grid[rows - 1][cols - 1];
    }
}
```

---

# 📊 Example Walkthrough

Given:

```text
1 3 1
1 5 1
4 2 1
```

After processing:

```text
1 4 5
2 7 6
6 8 7
```

The answer is:

```text
7
```

Corresponding path:

```text
1 → 3 → 1 → 1 → 1
```

---

# 📊 Complexity Analysis

| Metric | Complexity   |
| ------ | ------------ |
| Time   | **O(m × n)** |
| Space  | **O(1)**     |

Where:

* **m** = number of rows
* **n** = number of columns

---

# 🚀 Why This Solution Is Optimal

* Every cell is visited exactly once.
* No unnecessary recalculations are performed.
* No additional DP matrix is allocated.
* The algorithm achieves the optimal time complexity while minimizing extra memory usage.

---

# 🎯 Key Concepts

* Dynamic Programming
* Matrix Traversal
* State Transition
* In-place Optimization
* Grid Problems

---

# 📚 Lessons Learned

* Many grid problems can be solved using Dynamic Programming.
* Updating the input grid in place is an effective space optimization when modifying the input is allowed.
* Defining a clear DP state and transition formula simplifies implementation.

---

# 🔗 Related Problems

* 62. Unique Paths
* 63. Unique Paths II
* 120. Triangle
* 931. Minimum Falling Path Sum
* 221. Maximal Square

---

### 👨‍💻 Author

**Jeremiah Ogingo**

Software Engineering Student • Backend Developer • Problem Solver
