# ♛ N-Queens

[![LeetCode](https://img.shields.io/badge/LeetCode-51-orange?style=flat-square\&logo=leetcode)](https://leetcode.com/problems/n-queens/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=flat-square)](https://leetcode.com/problems/n-queens/)
[![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square\&logo=python)](https://www.python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Backtracking-purple?style=flat-square)](https://leetcode.com/problems/n-queens/)

## 📌 Overview

**N-Queens** is a classic **constraint-satisfaction and backtracking** problem.

The goal is to place `n` queens on an `n × n` chessboard so that no two queens can attack each other.

Since queens can attack horizontally, vertically, and diagonally, every valid configuration must satisfy three constraints:

* No two queens share the same row.
* No two queens share the same column.
* No two queens share the same diagonal.

The solution uses **backtracking** to construct valid configurations row by row while immediately abandoning placements that violate any constraint.

---

## 🧠 Core Idea

Instead of generating complete board configurations and checking them afterward, we validate each queen placement **before continuing**.

Because there can only be one queen in each row, the algorithm processes one row at a time:

```text
Choose a column
      ↓
Check whether the position is safe
      ↓
Place the queen
      ↓
Recursively solve the next row
      ↓
Undo the placement
      ↓
Try the next column
```

This follows the classic backtracking pattern:

> **Choose → Explore → Undo**

---

## 🧩 Data Structures

Three sets are used to perform constant-time conflict detection.

### 1. Columns

```python
columns = set()
```

Stores columns that already contain queens.

A position `(row, col)` is invalid when:

```python
col in columns
```

---

### 2. Positive Diagonals

```python
positive_diagonals = set()
```

For diagonals running from top-right to bottom-left:

```text
/
```

we use:

```python
row + col
```

Cells on the same diagonal have the same sum.

Example:

```text
(0, 2) → 0 + 2 = 2
(1, 1) → 1 + 1 = 2
(2, 0) → 2 + 0 = 2
```

Therefore, they belong to the same diagonal.

---

### 3. Negative Diagonals

```python
negative_diagonals = set()
```

For diagonals running from top-left to bottom-right:

```text
\
```

we use:

```python
row - col
```

Example:

```text
(0, 0) → 0 - 0 = 0
(1, 1) → 1 - 1 = 0
(2, 2) → 2 - 2 = 0
```

These cells are on the same diagonal.

---

## ⚙️ Algorithm

1. Create an empty `n × n` chessboard.
2. Start at row `0`.
3. Try placing a queen in every column of the current row.
4. Check whether the column and both diagonals are free.
5. If the position is safe:

   * Place the queen.
   * Mark its column and diagonals as occupied.
   * Recursively process the next row.
6. When the recursive call returns, remove the queen and release its constraints.
7. When all `n` rows contain queens, convert the board into strings and store the solution.
8. Return all valid configurations.

---

## 💻 Implementation

```python
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        # Create an empty chessboard.
        board = [["."] * n for _ in range(n)]

        # Track occupied columns and diagonals.
        columns = set()
        positive_diagonals = set()  # row + col
        negative_diagonals = set()  # row - col

        def backtrack(row: int) -> None:
            # All queens have been successfully placed.
            if row == n:
                result.append(
                    ["".join(row) for row in board]
                )
                return

            # Try every column in the current row.
            for col in range(n):

                # Check whether the position is attacked.
                if (
                    col in columns
                    or (row + col) in positive_diagonals
                    or (row - col) in negative_diagonals
                ):
                    continue

                # Place the queen.
                board[row][col] = "Q"
                columns.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)

                # Explore the next row.
                backtrack(row + 1)

                # Backtrack.
                board[row][col] = "."
                columns.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)

        backtrack(0)

        return result
```

---

## 🔍 Example Walkthrough

### Input

```text
n = 4
```

A valid configuration is:

```text
.Q..
...Q
Q...
..Q.
```

The queens are located at:

```text
(0,1)
(1,3)
(2,0)
(3,2)
```

### Constraint verification

**Columns:**

```text
1, 3, 0, 2
```

All are different.

**Positive diagonals (`row + col`):**

```text
1, 4, 2, 5
```

All are different.

**Negative diagonals (`row - col`):**

```text
-1, -2, 2, 1
```

All are different.

Therefore, no queen can attack another queen.

For `n = 4`, the algorithm finds **2 distinct solutions**.

---

## ⏱️ Complexity Analysis

| Metric              | Complexity                     |
| ------------------- | ------------------------------ |
| Backtracking Search | `O(N!)` approximately          |
| Board Construction  | `O(N²)` per solution           |
| Auxiliary Space     | `O(N)`                         |
| Output Space        | Depends on number of solutions |

The `O(N!)` estimate comes from exploring permutations of column choices while pruning invalid branches.

The three sets allow each placement to be validated in **O(1)** time instead of scanning the board.

---

## 🚀 Why This Approach Is Efficient

A naive solution could generate every possible arrangement and check whether each arrangement is valid afterward.

That approach performs a large amount of unnecessary work.

The backtracking solution performs **early pruning**:

```text
Invalid placement
      ↓
Stop exploring this branch
      ↓
Try another position
```

This dramatically reduces the search space.

The combination of:

* Backtracking
* One queen per row
* Column tracking
* Diagonal tracking
* Early constraint checking

makes this an efficient solution for the problem's constraints.

---

## 💡 Implementation Highlights

### One Queen Per Row

The algorithm recursively advances one row at a time:

```python
backtrack(row + 1)
```

Therefore, there is never a need to explicitly check whether another queen exists in the same row.

### Constant-Time Constraint Checking

Instead of scanning the board:

```python
if (
    col in columns
    or (row + col) in positive_diagonals
    or (row - col) in negative_diagonals
):
    continue
```

Each constraint can be checked using a set lookup.

### In-Place Backtracking

The same board is reused throughout the search.

```python
board[row][col] = "Q"

backtrack(row + 1)

board[row][col] = "."
```

This avoids creating a new board for every recursive branch.

---

## 📚 Lessons Learned

* Backtracking is useful for **constraint-satisfaction problems**.
* Invalid choices should be rejected as early as possible.
* A problem involving diagonals can often be simplified using mathematical coordinates.
* `row + col` uniquely identifies one diagonal direction.
* `row - col` uniquely identifies the opposite diagonal direction.
* Sets provide efficient membership checks for occupied positions.
* The **Choose → Explore → Undo** pattern is fundamental to recursive search.
* In-place modification can significantly reduce auxiliary memory usage.

---

## 🔑 Key Pattern

### Backtracking Template

```python
def backtrack(state):
    if is_complete(state):
        save_solution(state)
        return

    for choice in choices:
        if not valid(choice):
            continue

        make_choice(choice)
        backtrack(state)
        undo_choice(choice)
```

For N-Queens:

```text
State     → Current board
Choice    → Column for the current row
Constraint → Column + two diagonals
Explore   → Next row
Undo      → Remove queen
```

---

## 🧠 Related Concepts

* Backtracking
* Recursion
* Constraint Satisfaction
* Depth-First Search
* Hash Sets
* Matrix Traversal
* Diagonal Indexing
* Search Space Pruning
* Combinatorial Optimization

---

## 🔗 Related LeetCode Problems

* [N-Queens II — #52](https://leetcode.com/problems/n-queens-ii/)
* [Sudoku Solver — #37](https://leetcode.com/problems/sudoku-solver/)
* [Word Search — #79](https://leetcode.com/problems/word-search/)
* [Permutations — #46](https://leetcode.com/problems/permutations/)
* [Combinations — #77](https://leetcode.com/problems/combinations/)

These problems reinforce the same fundamental ideas of **recursive exploration, constraint checking, and backtracking**.

---

## 📝 Notes

* The board uses `"."` for an empty position and `"Q"` for a queen.
* Exactly one queen is placed in every row.
* Column conflicts are tracked using `col`.
* Diagonal conflicts are tracked using `row + col` and `row - col`.
* The board is modified in place and restored after each recursive branch.
* The solution returns **all distinct valid configurations**, not just the number of solutions.

---

## 📖 Reference

* [LeetCode — N-Queens #51](https://leetcode.com/problems/n-queens/)
* [Python Documentation](https://docs.python.org/3/)
* [Backtracking — Algorithmic Technique](https://en.wikipedia.org/wiki/Backtracking)

---

## 👨‍💻 Repository Structure

```text
LeetCode-Solutions/
│
├── Easy/
├── Medium/
└── Hard/
    └── Python/
        └── N-Queens/
            ├── solution.py
            └── README.md
```

---

<div align="center">

### ♛ Mastering Backtracking, One Constraint at a Time

**LeetCode #51 • Hard • Python • Backtracking**

</div>
