# 289. Game of Life

<div align="center">

![LeetCode](https://img.shields.io/badge/LeetCode-289-orange?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Technique](https://img.shields.io/badge/Technique-In--Place%20Simulation-blue?style=for-the-badge)
![Space](https://img.shields.io/badge/Extra%20Space-O(1)-green?style=for-the-badge)

**In-place matrix simulation using state encoding to preserve the original generation.**

</div>

---

## 1. Problem Overview

**[LeetCode 289 – Game of Life](https://leetcode.com/problems/game-of-life/)**

The Game of Life is a cellular automaton devised by mathematician John Conway.

You are given an `m × n` binary matrix called `board`, where:

- `1` represents a live cell.
- `0` represents a dead cell.

Each cell interacts with its eight neighboring cells. Its state in the next generation depends on the number of currently live neighbors.

### Rules of the Game

The next state of each cell follows four rules:

| Current State | Live Neighbors | Next State | Rule |
|---|---:|---|---|
| Alive | Fewer than 2 | Dead | Underpopulation |
| Alive | 2 or 3 | Alive | Survival |
| Alive | More than 3 | Dead | Overpopulation |
| Dead | Exactly 3 | Alive | Reproduction |

All cell transitions must happen **simultaneously**.

### The Main Challenge

Updating cells immediately creates a problem: changing one cell may affect the neighbor count of another cell that has not yet been processed.

The challenge is to calculate the next generation without losing access to the original generation.

The optimal in-place approach solves this by temporarily encoding both the original and next states in the same matrix.

---

## 2. Core Idea: In-Place State Encoding

A straightforward solution would create a second matrix to store the next generation.

For an `m × n` matrix, this requires:

- Time: `O(m × n)`
- Auxiliary space: `O(m × n)`

Instead, we can reuse the original matrix by introducing two temporary values.

### State Representation

During the first traversal, a cell can have four possible values:

| Value | Original State | Next State | Meaning |
|---:|---|---|---|
| `0` | Dead | Dead | Remains dead |
| `1` | Alive | Alive | Remains alive |
| `2` | Alive | Dead | Will die |
| `-1` | Dead | Alive | Will become alive |

The temporary values preserve information about the original generation while recording the next generation.

### Why Use `2`?

```javascript
2 = Alive → Dead
```

Although the cell will eventually become dead, it was originally alive.

Therefore, it must still be counted as a live neighbor during the first traversal.

### Why Use `-1`?

```javascript
-1 = Dead → Alive
```

Although the cell will eventually become alive, it was originally dead.

It must not be counted as a live neighbor during the first traversal.

### Identifying Originally Live Cells

```javascript
if (cell === 1 || cell === 2) {
    liveNeighbors++;
}
```

Both values represent cells that were alive in the original generation.

This is the key to preserving simultaneous updates.

---

## 3. Algorithm

Every cell has up to eight neighbors:

```text
↖  ↑  ↗
←  X  →
↙  ↓  ↘
```

We use two passes through the matrix.

### Pass 1: Calculate and Encode Transitions

**Step 1 — Define the eight directions**

```javascript
const directions = [
    [-1, -1], [-1, 0], [-1, 1],
    [ 0, -1],           [ 0, 1],
    [ 1, -1], [ 1, 0],  [ 1, 1]
];
```

Each pair represents the row and column offset of a neighboring cell.

**Step 2 — Count originally live neighbors**

For every cell:

1. Visit its eight possible neighbors.
2. Check whether each neighbor is within the matrix boundaries.
3. Count neighbors whose values are either `1` or `2`.

**Step 3 — Apply the Game of Life rules**

For an originally live cell:

- Fewer than two live neighbors: mark it `2`.
- Two or three live neighbors: leave it as `1`.
- More than three live neighbors: mark it `2`.

For an originally dead cell:

- Exactly three live neighbors: mark it `-1`.
- Otherwise, leave it as `0`.

These temporary values preserve the original state throughout the first pass.

### Pass 2: Finalize the Next Generation

After every cell has been processed, convert the temporary values:

```text
2  →  0
-1 →  1
```

The matrix now contains the next generation.

---

## 4. JavaScript Solution

```javascript
/**
 * LeetCode 289 - Game of Life
 *
 * @param {number[][]} board
 * @return {void}
 * Modifies the board in-place.
 */
var gameOfLife = function (board) {
    if (!board.length || !board[0].length) return;

    const rows = board.length;
    const cols = board[0].length;

    // All eight possible neighboring directions.
    const directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [ 0, -1],           [ 0, 1],
        [ 1, -1], [ 1, 0],  [ 1, 1]
    ];

    // Count neighbors that were originally alive.
    function countLiveNeighbors(row, col) {
        let liveNeighbors = 0;

        for (const [dr, dc] of directions) {
            const newRow = row + dr;
            const newCol = col + dc;

            // Ensure the neighboring cell is within bounds.
            if (
                newRow >= 0 &&
                newRow < rows &&
                newCol >= 0 &&
                newCol < cols
            ) {
                const cell = board[newRow][newCol];

                // 1 = originally alive
                // 2 = originally alive, but will die
                if (cell === 1 || cell === 2) {
                    liveNeighbors++;
                }
            }
        }

        return liveNeighbors;
    }

    // First pass: calculate and encode next-generation states.
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const liveNeighbors = countLiveNeighbors(row, col);

            if (board[row][col] === 1) {
                // Live cell dies from underpopulation or overpopulation.
                if (liveNeighbors < 2 || liveNeighbors > 3) {
                    board[row][col] = 2;
                }
            } else {
                // Dead cell becomes alive through reproduction.
                if (liveNeighbors === 3) {
                    board[row][col] = -1;
                }
            }
        }
    }

    // Second pass: convert temporary states into final states.
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (board[row][col] === 2) {
                board[row][col] = 0;
            } else if (board[row][col] === -1) {
                board[row][col] = 1;
            }
        }
    }
};
```

---

## 5. Example and Dry Run

### Example 1

**Input:**

```javascript
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
];
```

**First Pass: Temporary State Encoding**

After calculating the next state of every cell:

```javascript
[
    [0,  2, 0],
    [-1, 0, 1],
    [1,  1, 1],
    [0, -1, 0]
];
```

The temporary values represent:

```text
2  = Alive → Dead
-1 = Dead  → Alive
```

**Second Pass: Finalize the Matrix**

Convert `2` to `0` and `-1` to `1`.

**Output:**

```javascript
[
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0]
];
```

The final matrix represents the next generation.

### Example 2: Isolated Live Cell

**Input:**

```javascript
board = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
];
```

The live cell has zero live neighbors.

According to the underpopulation rule, it dies.

**Output:**

```javascript
[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
];
```

---

## 6. Complexity Analysis

Let:

- `m` = number of rows.
- `n` = number of columns.

### Time Complexity

\[
O(m \times n)
\]

Each cell is visited twice:

1. The first pass examines at most eight neighbors per cell.
2. The second pass finalizes temporary states.

Since each cell has a fixed maximum of eight neighbors, the total work is proportional to the number of cells.

### Auxiliary Space Complexity

\[
O(1)
\]

The algorithm does not create another matrix or a data structure proportional to the input size.

The directions array contains only eight fixed coordinate pairs, and the neighbor-counting function uses a constant amount of additional memory.

### Approach Comparison

| Approach | Time Complexity | Auxiliary Space |
|---|---|---|
| Create a new matrix | O(m × n) | O(m × n) |
| In-place state encoding | O(m × n) | O(1) |

The in-place approach provides the same time complexity while reducing auxiliary space to constant space.

---

## 7. Common Mistakes

### 1. Updating Cells Immediately

Incorrect:

```javascript
if (shouldDie) {
    board[row][col] = 0;
}
```

This destroys information that neighboring cells may still need.

**Solution:** Use temporary states and finalize the board only after processing every cell.

### 2. Counting Newly Alive Cells

A cell marked `-1` was originally dead.

It must not be counted as a live neighbor during the first pass.

### 3. Forgetting Cells Marked as `2`

A cell marked `2` was originally alive.

It must still contribute to the live-neighbor count.

Correct condition:

```javascript
cell === 1 || cell === 2
```

### 4. Ignoring Matrix Boundaries

Cells on the edges and corners have fewer than eight valid neighbors.

Always validate row and column indices before accessing a neighboring cell.

```javascript
newRow >= 0 &&
newRow < rows &&
newCol >= 0 &&
newCol < cols
```

### 5. Using the Wrong Transition Conditions

Remember the exact rules:

- Alive with fewer than two neighbors dies.
- Alive with two or three neighbors survives.
- Alive with more than three neighbors dies.
- Dead with exactly three neighbors becomes alive.

---

## 8. Implementation Highlights

| Property | Implementation |
|---|---|
| Problem | LeetCode 289 |
| Language | JavaScript ES6+ |
| Category | Matrix Simulation |
| Technique | In-Place State Encoding |
| Traversal | Two-Pass Matrix Traversal |
| Neighbor Evaluation | Eight Directions |
| Time Complexity | O(m × n) |
| Auxiliary Space | O(1) |
| Main Challenge | Simultaneous State Transitions |

---

## 9. Lessons Learned

### Preserve Original Information

When multiple updates must happen simultaneously, modifying values immediately may destroy information needed by later operations.

Temporary state encoding allows both the original and next states to coexist.

### Use Input as Temporary Storage

An existing data structure can sometimes store intermediate information without requiring another matrix.

This is particularly useful when a problem imposes strict auxiliary-space requirements.

### Recognize the Two-Pass Pattern

A useful general pattern for in-place algorithms is:

```text
Original State
      ↓
Calculate Transitions
      ↓
Encode Temporary States
      ↓
Finalize Changes
```

This separates the calculation of changes from the application of those changes.

### Expand the State Representation

A binary matrix normally contains two possible values: `0` and `1`.

Introducing temporary values allows us to represent four possible transitions without losing the original state.

---

## 10. Generalization: Infinite Game of Life Board

The standard implementation uses a finite two-dimensional matrix.

For an effectively infinite board, allocating a large matrix would be inefficient, especially when only a small proportion of cells are alive.

A better representation is a sparse data structure, such as a JavaScript `Set`, containing the coordinates of live cells.

Example:

```javascript
const liveCells = new Set([
    "2,3",
    "5,7",
    "10,4"
]);
```

Instead of representing every possible cell, only live coordinates are stored.

For each generation:

1. Visit every currently live cell.
2. Count its contribution to the eight neighboring positions.
3. Track neighbor counts for candidate cells.
4. Apply the Game of Life rules to determine the next set of live coordinates.

This approach is more practical for sparse, effectively unbounded boards.

**Important:** The sparse representation is a different approach. Its memory usage depends on the number of active cells and their neighboring candidate positions; it does not retain the O(1) auxiliary-space property of the finite-board implementation.

---

## 11. Related Concepts

- Matrix Simulation
- In-Place Algorithms
- State Encoding
- Cellular Automata
- Two-Pass Algorithms
- Space Optimization
- Grid Traversal
- Neighbor Enumeration

## 12. Related LeetCode Problems

| Problem | Difficulty | Main Concept |
|---|---|---|
| [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | In-Place Markers |
| [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | In-Place Matrix |
| [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | Matrix Traversal |
| [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | Grid Traversal |
| [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Matrix + DFS/BFS |

---

## 13. References

- [LeetCode – 289. Game of Life](https://leetcode.com/problems/game-of-life/)
- [Conway's Game of Life – Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

---

<div align="center">

### Problem #289 — Game of Life

**Difficulty:** Medium

**Language:** JavaScript

**Time Complexity:** O(m × n)

**Auxiliary Space:** O(1)

**Key Pattern:**

`Read Original State → Encode Transition → Finalize State`

⭐ Keep solving. Keep learning. Keep improving.

</div>