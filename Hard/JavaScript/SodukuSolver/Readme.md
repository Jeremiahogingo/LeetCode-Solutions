# 🧩 37. Sudoku Solver

<div align="center">

![LeetCode](https://img.shields.io/badge/LeetCode-37-orange?style=for-the-badge\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![Algorithm](https://img.shields.io/badge/Algorithm-Backtracking-blue?style=for-the-badge)
![Data Structure](https://img.shields.io/badge/Data%20Structure-Hash%20Set-green?style=for-the-badge)

**A JavaScript solution using Backtracking and efficient constraint tracking.**

</div>

---

## 📖 Overview

This solution completes a partially filled Sudoku board using **backtracking**.

Instead of trying every possible configuration blindly, the algorithm progressively fills empty cells while maintaining the Sudoku constraints.

If a choice eventually leads to an invalid state, the algorithm reverses that choice and tries another possibility.

The implementation uses:

* 🔄 Backtracking
* #️⃣ JavaScript `Set`
* 🧮 Constraint checking
* 🗂️ Matrix traversal
* ♻️ In-place board modification

---

## 💡 Core Idea

The algorithm follows the classic backtracking pattern:

```text
Choose a number
      ↓
Check whether valid
      ↓
Place the number
      ↓
Solve the next cell
      ↓
   Successful?
    ↙      ↘
  Yes       No
   ↓         ↓
 Done      Undo
             ↓
         Try another
```

For every empty cell, the algorithm attempts the digits `1` through `9`.

A digit can only be placed if it does not already exist in:

* The current row
* The current column
* The current 3×3 box

---

## 🧠 Constraint Tracking

Three arrays of JavaScript `Set` objects are used:

```javascript
const rows = Array.from(
    { length: 9 },
    () => new Set()
);

const cols = Array.from(
    { length: 9 },
    () => new Set()
);

const boxes = Array.from(
    { length: 9 },
    () => new Set()
);
```

Each set stores the digits currently used in its corresponding region.

### Row

```javascript
rows[r]
```

Tracks the digits already present in row `r`.

### Column

```javascript
cols[c]
```

Tracks the digits already present in column `c`.

### 3 × 3 Box

The box containing a cell is calculated using:

```javascript
const box =
    Math.floor(r / 3) * 3 +
    Math.floor(c / 3);
```

The resulting box indices are:

```text
+-------+-------+-------+
|   0   |   1   |   2   |
+-------+-------+-------+
|   3   |   4   |   5   |
+-------+-------+-------+
|   6   |   7   |   8   |
+-------+-------+-------+
```

---

## ⚙️ Algorithm

### 1. Initialize the Board

Traverse all 81 cells.

For every filled cell:

* Add its value to the corresponding row set.
* Add its value to the corresponding column set.
* Add its value to the corresponding box set.

For every empty cell, store its coordinates in an `empty` array.

---

### 2. Start Backtracking

Take the next empty cell and calculate its box.

Try every digit from:

```text
1 → 9
```

Before placing a digit, check:

```javascript
rows[r].has(value)
cols[c].has(value)
boxes[box].has(value)
```

If the digit exists in any of these sets, skip it.

---

### 3. Make a Choice

When a valid digit is found:

```javascript
board[r][c] = value;
```

The digit is also added to the appropriate sets.

The algorithm then recursively processes the next empty cell.

---

### 4. Backtrack

If the recursive call cannot find a valid solution:

```javascript
board[r][c] = ".";
```

The digit is removed from:

```javascript
rows[r]
cols[c]
boxes[box]
```

The algorithm then tries another digit.

---

### 5. Complete the Board

When all empty cells have been successfully filled:

```javascript
if (index === empty.length) {
    return true;
}
```

The solution has been found.

---

## 🟨 JavaScript Solution

```javascript
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function (board) {

    const rows = Array.from(
        { length: 9 },
        () => new Set()
    );

    const cols = Array.from(
        { length: 9 },
        () => new Set()
    );

    const boxes = Array.from(
        { length: 9 },
        () => new Set()
    );

    const empty = [];

    // Initialize sets and collect empty cells
    for (let r = 0; r < 9; r++) {

        for (let c = 0; c < 9; c++) {

            const value = board[r][c];

            if (value === ".") {
                empty.push([r, c]);
                continue;
            }

            const box =
                Math.floor(r / 3) * 3 +
                Math.floor(c / 3);

            rows[r].add(value);
            cols[c].add(value);
            boxes[box].add(value);
        }
    }

    function backtrack(index) {

        // All empty cells have been filled
        if (index === empty.length) {
            return true;
        }

        const [r, c] = empty[index];

        const box =
            Math.floor(r / 3) * 3 +
            Math.floor(c / 3);

        // Try digits 1 through 9
        for (let digit = 1; digit <= 9; digit++) {

            const value = String(digit);

            // Check whether the digit is already used
            if (
                rows[r].has(value) ||
                cols[c].has(value) ||
                boxes[box].has(value)
            ) {
                continue;
            }

            // Make the choice
            board[r][c] = value;

            rows[r].add(value);
            cols[c].add(value);
            boxes[box].add(value);

            // Continue solving
            if (backtrack(index + 1)) {
                return true;
            }

            // Undo the choice
            board[r][c] = ".";

            rows[r].delete(value);
            cols[c].delete(value);
            boxes[box].delete(value);
        }

        return false;
    }

    backtrack(0);
};
```

---

## 🔍 Why `Set` Is Used

JavaScript's `Set` provides convenient membership operations:

```javascript
rows[r].has(value)
```

Adding:

```javascript
rows[r].add(value)
```

Removing:

```javascript
rows[r].delete(value)
```

This makes constraint checking clean and efficient.

---

## 📊 Complexity Analysis

Let `E` represent the number of empty cells.

### Time Complexity

The worst-case backtracking search can be exponential:

```text
O(9^E)
```

However, constraint checking eliminates invalid candidates early, making the practical performance significantly better.

### Space Complexity

The recursion stack can reach:

```text
O(E)
```

The row, column, and box sets have a fixed maximum size because Sudoku always uses a 9×9 board.

Therefore:

```text
Auxiliary Space: O(E)
```

---

## 🚀 Implementation Highlights

* Uses **JavaScript ES6+**.
* Uses native `Set` objects for constraint tracking.
* Uses recursive DFS-style backtracking.
* Stores empty cells before starting the search.
* Modifies the board **in place**.
* Immediately stops once a valid solution is found.
* Uses explicit undo operations to restore the previous state.

---

## 🧠 Backtracking Pattern

The general pattern used here is:

```text
1. Find an unresolved position
2. Generate possible choices
3. Reject invalid choices
4. Make a valid choice
5. Recursively explore
6. Undo the choice if exploration fails
7. Continue until a solution is found
```

This pattern is useful beyond Sudoku and appears in:

* N-Queens
* Word Search
* Permutations
* Combinations
* Maze solving
* Graph coloring
* Constraint satisfaction problems

---

## 🎯 Lessons Learned

### 1. Backtracking is optimized search

Backtracking explores possibilities while eliminating invalid branches as early as possible.

### 2. Every choice needs an undo operation

A backtracking algorithm generally follows:

```javascript
makeChoice();
explore();
undoChoice();
```

### 3. Data structures can reduce repeated work

Using `Set` allows the algorithm to quickly determine whether a candidate digit is already being used.

### 4. Recursion naturally models the problem

Each recursive call represents the task of solving the remaining empty cells.

---

## 🔗 Related Problems

* [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
* [51. N-Queens](https://leetcode.com/problems/n-queens/)
* [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)
* [79. Word Search](https://leetcode.com/problems/word-search/)
* [980. Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)

---

## 🔗 Reference

**LeetCode:** [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

---

<div align="center">

### 🧠 Algorithm: Backtracking + Constraint Tracking

**Difficulty:** Hard
**Language:** JavaScript (ES6+)

⭐ Keep solving. Keep learning. Keep improving.

</div>
