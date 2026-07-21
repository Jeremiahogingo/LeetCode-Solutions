# 🎯 36. Valid Sudoku

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)
![Topics](https://img.shields.io/badge/Topics-Hash%20Table%20%7C%20Matrix-blue)

## 📖 Overview

This problem focuses on validating a partially filled Sudoku board.

The objective is **not** to solve the Sudoku puzzle, but to determine whether the current board configuration satisfies all Sudoku constraints.

A valid board must ensure that every filled digit appears only once in:

* Each row
* Each column
* Each 3×3 sub-grid

Empty cells (`.`) are ignored during validation.

---

# 💡 Core Idea

While traversing the board once, keep track of every digit that has already appeared.

Instead of repeatedly scanning rows and columns, use **hash sets** for constant-time lookups.

Three collections are maintained:

* One for every row
* One for every column
* One for every 3×3 box

Whenever a duplicate is encountered, the board is immediately invalid.

---

# 🧠 Data Structures

The solution uses three arrays of sets.

```text
rows[9]
cols[9]
boxes[9]
```

Each set stores the digits already seen within its corresponding region.

The index of a 3×3 box is computed using:

```python
box = (row // 3) * 3 + (col // 3)
```

Resulting layout:

```text
0 0 0 | 1 1 1 | 2 2 2
0 0 0 | 1 1 1 | 2 2 2
0 0 0 | 1 1 1 | 2 2 2
------+-------+------
3 3 3 | 4 4 4 | 5 5 5
3 3 3 | 4 4 4 | 5 5 5
3 3 3 | 4 4 4 | 5 5 5
------+-------+------
6 6 6 | 7 7 7 | 8 8 8
6 6 6 | 7 7 7 | 8 8 8
6 6 6 | 7 7 7 | 8 8 8
```

---

# ⚙️ Algorithm

1. Create nine sets for rows.
2. Create nine sets for columns.
3. Create nine sets for sub-boxes.
4. Traverse every cell.
5. Ignore empty cells.
6. Compute the corresponding box index.
7. If the digit already exists in its row, column, or box, return `False`.
8. Otherwise, insert the digit into all three sets.
9. After processing the board, return `True`.

---

# 🐍 Python Solution

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                if value == ".":
                    continue

                box = (r // 3) * 3 + (c // 3)

                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in boxes[box]
                ):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True
```

---

# ☕ Java Solution

```java
class Solution {

    public boolean isValidSudoku(char[][] board) {

        HashSet<Character>[] rows = new HashSet[9];
        HashSet<Character>[] cols = new HashSet[9];
        HashSet<Character>[] boxes = new HashSet[9];

        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }

        for (int r = 0; r < 9; r++) {

            for (int c = 0; c < 9; c++) {

                char value = board[r][c];

                if (value == '.')
                    continue;

                int box = (r / 3) * 3 + (c / 3);

                if (
                    rows[r].contains(value) ||
                    cols[c].contains(value) ||
                    boxes[box].contains(value)
                ) {
                    return false;
                }

                rows[r].add(value);
                cols[c].add(value);
                boxes[box].add(value);
            }
        }

        return true;
    }
}
```

---

# 📊 Complexity Analysis

| Metric | Complexity           |
| ------ | -------------------- |
| Time   | **O(81)** → **O(1)** |
| Space  | **O(81)** → **O(1)** |

Since the Sudoku board always contains exactly **81 cells**, both time and space are constant.

---

# 🎯 Key Concepts

* Hash Sets
* Matrix Traversal
* Constant-Time Lookup
* Constraint Validation
* Simulation

---

# 📚 Lessons Learned

* Hash sets provide an efficient way to detect duplicates in constant time.
* Mapping each cell to its 3×3 box simplifies validation.
* Some problems have constant complexity because their input size is fixed, even if the algorithm contains nested loops.

---

# 🔗 Related Problems

* 37. Sudoku Solver
* 73. Set Matrix Zeroes
* 48. Rotate Image
* 289. Game of Life

---

### 👨‍💻 Author

**Jeremiah Ogingo**

Software Engineering Student • Backend Developer • Problem Solver
