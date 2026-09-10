# ♛ N-Queens II

[![LeetCode](https://img.shields.io/badge/LeetCode-52-orange?style=flat-square\&logo=leetcode)](https://leetcode.com/problems/n-queens-ii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=flat-square)](https://leetcode.com/problems/n-queens-ii/)
[![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square\&logo=python)](https://www.python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Backtracking-purple?style=flat-square)](https://leetcode.com/problems/n-queens-ii/)

## 📌 Overview

**N-Queens II** is the counting variant of the classic **N-Queens** problem.

The objective is to determine the **number of distinct ways** to place `n` queens on an `n × n` chessboard such that no two queens can attack each other.

Queens cannot share:

* The same row
* The same column
* The same diagonal

Unlike **N-Queens #51**, this problem does not require returning the actual board configurations. It only requires the total number of valid arrangements.

This allows us to eliminate the board representation and store only the information required to validate queen placements.

---

## 🧠 Core Idea

Use **backtracking** to place one queen in each row.

For every row, try each column and determine whether the position is safe.

A position is valid when:

```text
Column is free
        AND
Positive diagonal is free
        AND
Negative diagonal is free
```

If the position is valid:

```text
Place Queen
     ↓
Explore next row
     ↓
Count valid solutions
     ↓
Remove Queen
     ↓
Try next position
```

This follows the classic:

> **Choose → Explore → Undo**

backtracking pattern.

---

## 🧩 Data Structures

Three sets are used to track occupied positions.

### 1. Columns

```python
columns = set()
```

Stores columns containing queens.

```python
col in columns
```

detects a column conflict in `O(1)` average time.

---

### 2. Positive Diagonals

```python
positive_diagonals = set()
```

The diagonal:

```text
/
```

is identified using:

```python
row + col
```

For example:

```text
(0, 2) → 0 + 2 = 2
(1, 1) → 1 + 1 = 2
(2, 0) → 2 + 0 = 2
```

All belong to the same diagonal.

---

### 3. Negative Diagonals

```python
negative_diagonals = set()
```

The diagonal:

```text
\
```

is identified using:

```python
row - col
```

For example:

```text
(0, 0) → 0 - 0 = 0
(1, 1) → 1 - 1 = 0
(2, 2) → 2 - 2 = 0
```

These cells belong to the same diagonal.

---

## ⚙️ Algorithm

1. Start at row `0`.
2. Try every column in the current row.
3. Check whether the column and both diagonals are available.
4. If the position is safe:

   * Mark the column.
   * Mark both diagonals.
   * Recursively process the next row.
5. When all `n` rows contain queens, return `1`.
6. Add the number of solutions returned by each valid branch.
7. Remove the queen's constraints and continue searching.
8. Return the total number of valid configurations.

---

## 💡 Why Return `1`?

This is the key difference between **N-Queens #51** and **N-Queens II #52**.

When every row has successfully received a queen:

```python
if row == n:
    return 1
```

The `1` means:

> **One complete valid configuration has been found.**

The parent call accumulates these values:

```python
solutions += backtrack(row + 1)
```

For example:

```text
                 Row 0
              /    |    \
             /     |     \
          valid   valid   invalid
            ↓       ↓
           ...     ...
            ↓       ↓
            1       1

             Total = 2
```

Therefore, we never need to construct or store the actual boards.

---

## 💻 Implementation

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = set()
        positive_diagonals = set()  # row + col
        negative_diagonals = set()  # row - col

        def backtrack(row: int) -> int:
            # All queens have been successfully placed.
            if row == n:
                return 1

            solutions = 0

            for col in range(n):
                # Check column and both diagonals.
                if (
                    col in columns
                    or (row + col) in positive_diagonals
                    or (row - col) in negative_diagonals
                ):
                    continue

                # Place queen.
                columns.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)

                # Explore the next row.
                solutions += backtrack(row + 1)

                # Backtrack.
                columns.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)

            return solutions

        return backtrack(0)
```

---

## 🔍 Example Walkthrough

### Input

```text
n = 4
```

There are two valid configurations:

```text
.Q..       ..Q.
...Q       Q...
Q...       ...Q
..Q.       .Q..
```

Instead of storing these configurations, the algorithm counts them.

Conceptually:

```text
First valid configuration → 1
Second valid configuration → 1

Total → 2
```

### Output

```text
2
```

---

## ⏱️ Complexity Analysis

| Metric          | Complexity              |
| --------------- | ----------------------- |
| Time            | **O(N!)** approximately |
| Auxiliary Space | **O(N)**                |
| Output Space    | **O(1)**                |

### Time Complexity

The backtracking search explores possible column placements for each row.

Because queens cannot share columns, the search is roughly bounded by permutations of column choices:

```text
N × (N - 1) × (N - 2) × ... × 1 = N!
```

Diagonal constraints prune many branches before they are fully explored.

### Space Complexity

The algorithm uses:

* `columns`
* `positive_diagonals`
* `negative_diagonals`
* recursion stack

Each requires at most `O(N)` space.

Therefore:

```text
Auxiliary Space = O(N)
```

There is no solution array or board stored because the problem only asks for a count.

---

## 🚀 Optimization Over N-Queens #51

The solution for **N-Queens II** can be viewed as a memory-optimized version of **N-Queens**.

### N-Queens #51

```text
Search
 ↓
Build board
 ↓
Convert board
 ↓
Store solution
 ↓
Return all solutions
```

### N-Queens II #52

```text
Search
 ↓
Find valid configuration
 ↓
Return 1
 ↓
Accumulate count
```

This removes the need for:

* A board
* String conversion
* A solution list
* Storing complete configurations

The backtracking search itself remains fundamentally the same.

---

## 🔑 Key Pattern

### Backtracking + Counting

The general pattern is:

```python
def backtrack(state):
    if is_complete(state):
        return 1

    count = 0

    for choice in choices:
        if not valid(choice):
            continue

        make_choice(choice)

        count += backtrack(next_state)

        undo_choice(choice)

    return count
```

For N-Queens II:

```text
State       → Current row
Choice      → Column
Constraint  → Column + two diagonals
Success     → row == n
Result      → Number of valid configurations
```

---

## 💡 Implementation Highlights

### One Queen Per Row

The recursive function processes exactly one row at a time:

```python
backtrack(row + 1)
```

Therefore, row conflicts do not need to be explicitly tracked.

### O(1) Average Conflict Detection

The sets allow direct membership checks:

```python
col in columns
row + col in positive_diagonals
row - col in negative_diagonals
```

### No Board Required

Unlike N-Queens #51, the board itself is unnecessary because the only required output is the number of solutions.

### In-Place State Management

The sets are modified and restored during backtracking:

```python
columns.add(col)

backtrack(row + 1)

columns.remove(col)
```

This keeps memory usage low.

---

## 📚 Lessons Learned

* Backtracking can be adapted from **solution generation** to **solution counting**.
* When only the number of solutions is required, storing complete solutions is unnecessary.
* `row + col` identifies one diagonal direction.
* `row - col` identifies the opposite diagonal direction.
* Sets provide efficient constraint checking.
* Returning `1` at a complete valid state provides a simple way to count solutions.
* Early pruning prevents unnecessary exploration of invalid configurations.
* The **Choose → Explore → Undo** pattern is fundamental to recursive search problems.

---

## 🧠 Related Concepts

* Backtracking
* Recursion
* Constraint Satisfaction
* Depth-First Search
* Combinatorics
* Hash Sets
* Search Space Pruning
* Diagonal Indexing
* Recursive Counting

---

## 🔗 Related LeetCode Problems

* [N-Queens — #51](https://leetcode.com/problems/n-queens/)
* [Sudoku Solver — #37](https://leetcode.com/problems/sudoku-solver/)
* [Word Search — #79](https://leetcode.com/problems/word-search/)
* [Permutations — #46](https://leetcode.com/problems/permutations/)
* [Combinations — #77](https://leetcode.com/problems/combinations/)

These problems reinforce recursive search, constraint validation, and backtracking techniques.

---

## 📝 Notes

* Exactly one queen is placed in every row.
* Column conflicts are tracked using `col`.
* Diagonal conflicts are tracked using `row + col` and `row - col`.
* The board does not need to be explicitly constructed.
* A complete valid arrangement contributes `1` to the total count.
* The algorithm returns the number of distinct solutions rather than the configurations themselves.
* This is the counting counterpart of **N-Queens #51**.

---

## 📖 Reference

* [LeetCode — N-Queens II #52](https://leetcode.com/problems/n-queens-ii/)
* [Python Documentation](https://docs.python.org/3/)
* [Backtracking — Wikipedia](https://en.wikipedia.org/wiki/Backtracking)

---

## 📂 Repository Structure

```text
LeetCode-Solutions/
│
├── Easy/
├── Medium/
└── Hard/
    └── Python/
        ├── N-Queens/
        │   ├── solution.py
        │   └── README.md
        │
        └── N-Queens-II/
            ├── solution.py
            └── README.md
```

---

<div align="center">

### ♛ Turning Search Into Counting

**LeetCode #52 • Hard • Python • Backtracking**

</div>
