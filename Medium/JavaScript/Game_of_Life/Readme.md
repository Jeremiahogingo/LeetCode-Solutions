📄 Complete Professional README.md

You can use the following directly in your repository:

# 289. Game of Life

📄 Complete Professional README.md

You can use the following directly in your repository:

# 289. Game of Life


<div align="center">


![LeetCode](https://img.shields.io/badge/LeetCode-289-orange?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Algorithm](https://img.shields.io/badge/Technique-In--Place%20Simulation-blue?style=for-the-badge)
![Space](https://img.shields.io/badge/Extra%20Space-O(1)-green?style=for-the-badge)


### In-place simulation using state encoding to preserve the original board.


</div>


---


## 📖 Overview


This problem is a simulation of **Conway's Game of Life**, where each cell in a two-dimensional board can either be:


- Alive (`1`)
- Dead (`0`)


The next generation of the board depends on the state of each cell and its eight neighboring cells.


The main challenge is that all cells must transition to their next state **simultaneously**.


This means we cannot immediately update a cell while traversing the board because neighboring cells may still need to access its original state.


The optimal solution solves this problem **in place** by temporarily encoding both the original and next states inside the existing board.


---


# 💡 Core Idea


A straightforward solution would create a second matrix.


For every cell:


1. Count its live neighbors.
2. Determine its next state.
3. Store the result in a new board.
4. Replace the original board.


Although simple, this requires:


```text
O(m × n) extra space

The optimal approach avoids creating another matrix.

Instead, we temporarily store state transitions directly inside the original board.

🧠 State Encoding

During processing, a cell can have one of four states:

Value	Original State	Next State
0	Dead	Dead
1	Alive	Alive
2	Alive	Dead
-1	Dead	Alive

The temporary values allow us to preserve the original state while calculating the next generation.

Why 2?
2 = Alive → Dead

Even though the cell will eventually die, it was originally alive.

Therefore, while counting neighbors:

cell === 1 || cell === 2

means the cell was originally alive.

Why -1?
-1 = Dead → Alive

Even though the cell will eventually become alive, it was originally dead.

Therefore, it should not be counted as a live neighbor during the first pass.

⚙️ Algorithm
Step 1 — Define the Eight Directions

Every cell can have up to eight neighbors:

↖  ↑  ↗
←  X  →
↙  ↓  ↘

These directions can be represented as:

const directions = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1]
];
Step 2 — Count Originally Live Neighbors

For each neighboring cell:

if (board[newRow][newCol] === 1 ||
    board[newRow][newCol] === 2)

count it as alive.

Both values represent cells that were alive in the original generation.

Step 3 — Apply State Transitions

For a live cell:

Live neighbors < 2
        ↓
Cell dies
Live neighbors = 2 or 3
        ↓
Cell survives
Live neighbors > 3
        ↓
Cell dies

For a dead cell:

Exactly 3 live neighbors
        ↓
Cell becomes alive
Step 4 — Use Temporary States

Instead of immediately converting:

1 → 0

store:

1 → 2

Instead of immediately converting:

0 → 1

store:

0 → -1

This preserves the original generation while processing the board.

Step 5 — Finalize the Board

After all cells have been processed:

2  →  0
-1 →  1

The board now represents the next generation.

🔍 Example
Input
[
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

During the first pass, some cells may temporarily become:

[
    [0, 2, 0],
    [-1, 0, 1],
    [1, 1, 1],
    [0, -1, 0]
]

Remember:

2  = alive → dead
-1 = dead → alive

After converting temporary states:

[
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0]
]
🧑‍💻 JavaScript Solution
/**
 * LeetCode 289 - Game of Life
 *
 * @param {number[][]} board
 * @return {void}
 * Do not return anything, modify board in-place instead.
 */
var gameOfLife = function (board) {
    const rows = board.length;
    const cols = board[0].length;


    // All possible directions around a cell
    const directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ];


    // Counts neighbors that were originally alive
    function countLiveNeighbors(row, col) {
        let liveNeighbors = 0;


        for (const [dr, dc] of directions) {
            const newRow = row + dr;
            const newCol = col + dc;


            // Ensure the neighbor is inside the board
            if (
                newRow >= 0 &&
                newRow < rows &&
                newCol >= 0 &&
                newCol < cols
            ) {
                // 1 = alive and remains alive
                // 2 = alive but will die
                if (
                    board[newRow][newCol] === 1 ||
                    board[newRow][newCol] === 2
                ) {
                    liveNeighbors++;
                }
            }
        }


        return liveNeighbors;
    }


    // First pass: determine transitions
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const liveNeighbors = countLiveNeighbors(row, col);


            // Originally alive
            if (board[row][col] === 1) {
                if (liveNeighbors < 2 || liveNeighbors > 3) {
                    // Alive -> Dead
                    board[row][col] = 2;
                }
            }


            // Originally dead
            else {
                if (liveNeighbors === 3) {
                    // Dead -> Alive
                    board[row][col] = -1;
                }
            }
        }
    }


    // Second pass: finalize transitions
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
📊 Complexity Analysis

Let:

m = number of rows
n = number of columns

Each cell checks at most eight neighbors.

Since eight is a constant:

Time Complexity
O(m × n)
Space Complexity
O(1)

No additional matrix or data structure proportional to the board size is created.

🔄 Approach Comparison
Approach	Time	Extra Space
Create a new board	O(m × n)	O(m × n)
Copy and update	O(m × n)	O(m × n)
In-place state encoding	O(m × n)	O(1)

The in-place approach is optimal in terms of auxiliary space.

⚠️ Common Mistakes
1. Updating Cells Immediately

This is incorrect:

if (shouldDie) {
    board[row][col] = 0;
}

The problem is that future cells may use this updated value when counting their neighbors.

The Game of Life requires all transitions to happen simultaneously.

The solution is:

Original State
      ↓
Temporary State
      ↓
Final State
2. Counting Newly Alive Cells

A cell marked:

-1

was originally dead.

Even though it will become alive, it must not be counted as a live neighbor during the first pass.

3. Forgetting Cells Marked as 2

A cell marked:

2

was originally alive.

Therefore, it must still be counted as a live neighbor.

if (cell === 1 || cell === 2)
4. Ignoring Board Boundaries

Cells near the edges have fewer than eight valid neighbors.

Always check:

newRow >= 0 &&
newRow < rows &&
newCol >= 0 &&
newCol < cols

before accessing a neighboring cell.

🚀 Implementation Highlights
Language: JavaScript ES6+
Technique: In-place state encoding
Category: Matrix Simulation
Traversal: Two-pass matrix traversal
Time Complexity: O(m × n)
Extra Space: O(1)
Key Challenge: Simultaneous state transitions
🧠 Lessons Learned
1. Preserve the Original State

When an algorithm requires simultaneous updates, modifying values immediately can destroy information needed later.

A useful strategy is to temporarily encode:

Old State + New State

inside the existing data structure.

2. Input Can Be Used as Temporary Storage

Instead of creating another matrix:

Original Board
+
New Board

we reuse the existing board.

This is a common technique in problems that require:

O(1) auxiliary space
3. Two-Pass Algorithms Are Useful for Simultaneous Updates

A common pattern is:

Pass 1
Determine and encode transitions
        ↓
Pass 2
Finalize transitions

This pattern appears in many in-place simulation and matrix problems.

4. Temporary Values Can Store State Transitions

Instead of thinking of a cell as having only:

Dead
Alive

we temporarily expand the possible states:

Dead → Dead
Alive → Alive
Alive → Dead
Dead → Alive

This makes it possible to remember both generations simultaneously.

🎯 Key Pattern
          ┌────────────────┐
          │ Original State │
          └───────┬────────┘
                  ↓
          ┌────────────────┐
          │ Encode Change  │
          └───────┬────────┘
                  ↓
          ┌────────────────┐
          │ Finalize State │
          └────────────────┘

When updates must happen simultaneously but extra space is restricted, encode both the old and new states directly inside the input.

🔗 Related Concepts
Matrix Simulation
In-Place Algorithms
State Encoding
Cellular Automata
Two-Pass Algorithms
Space Optimization
Grid Traversal
Neighbor Enumeration
🔗 Related LeetCode Problems
#	Problem	Difficulty	Main Concept
73	Set Matrix Zeroes	🟡 Medium	In-Place Markers
289	Game of Life	🟡 Medium	State Encoding
48	Rotate Image	🟡 Medium	In-Place Matrix
54	Spiral Matrix	🟡 Medium	Matrix Traversal
130	Surrounded Regions	🟡 Medium	Grid Traversal
200	Number of Islands	🟡 Medium	Matrix + DFS/BFS
🌍 Follow-Up: What About an Infinite Board?

The standard problem uses a finite 2D array, but the follow-up asks how an effectively infinite board could be handled when live cells reach the boundaries.

A practical approach would be to store only live cells in a sparse data structure, such as a Set or hash-based representation:

Set of live cell coordinates

For example:

"2,3"
"5,7"
"10,4"

Instead of storing an enormous grid:

1000000 × 1000000

we only store cells that are actually alive.

This is especially effective when the board is sparse.

📚 Reference

LeetCode — 289. Game of Life

The official problem defines the four transition rules, simultaneous updates, and the in-place follow-up.

📁 Recommended Repository Structure
LeetCode-Solutions/
│
├── medium/
│   └── matrix/
│       └── game-of-life/
│           ├── README.md
│           └── solution.js
│
├── notes/
│   ├── Patterns.md
│   ├── Complexity.md
│   ├── InPlaceAlgorithms.md
│   └── StateEncoding.md
│
└── README.md
<div align="center">
🧬 Problem #289

Difficulty: Medium
Language: JavaScript
Time Complexity: O(m × n)
Space Complexity: O(1)

🔑 Pattern

Read Original State → Encode Transition → Finalize State

⭐ Keep solving. Keep learning. Keep improving.

</div> ```
<div align="center">


![LeetCode](https://img.shields.io/badge/LeetCode-289-orange?style=for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Algorithm](https://img.shields.io/badge/Technique-In--Place%20Simulation-blue?style=for-the-badge)
![Space](https://img.shields.io/badge/Extra%20Space-O(1)-green?style=for-the-badge)


### In-place simulation using state encoding to preserve the original board.


</div>


---


## 📖 Overview


This problem is a simulation of **Conway's Game of Life**, where each cell in a two-dimensional board can either be:


- Alive (`1`)
- Dead (`0`)


The next generation of the board depends on the state of each cell and its eight neighboring cells.


The main challenge is that all cells must transition to their next state **simultaneously**.


This means we cannot immediately update a cell while traversing the board because neighboring cells may still need to access its original state.


The optimal solution solves this problem **in place** by temporarily encoding both the original and next states inside the existing board.


---


# 💡 Core Idea


A straightforward solution would create a second matrix.


For every cell:


1. Count its live neighbors.
2. Determine its next state.
3. Store the result in a new board.
4. Replace the original board.


Although simple, this requires:


```text
O(m × n) extra space

The optimal approach avoids creating another matrix.

Instead, we temporarily store state transitions directly inside the original board.

🧠 State Encoding

During processing, a cell can have one of four states:

Value	Original State	Next State
0	Dead	Dead
1	Alive	Alive
2	Alive	Dead
-1	Dead	Alive

The temporary values allow us to preserve the original state while calculating the next generation.

Why 2?
2 = Alive → Dead

Even though the cell will eventually die, it was originally alive.

Therefore, while counting neighbors:

cell === 1 || cell === 2

means the cell was originally alive.

Why -1?
-1 = Dead → Alive

Even though the cell will eventually become alive, it was originally dead.

Therefore, it should not be counted as a live neighbor during the first pass.

⚙️ Algorithm
Step 1 — Define the Eight Directions

Every cell can have up to eight neighbors:

↖  ↑  ↗
←  X  →
↙  ↓  ↘

These directions can be represented as:

const directions = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1]
];
Step 2 — Count Originally Live Neighbors

For each neighboring cell:

if (board[newRow][newCol] === 1 ||
    board[newRow][newCol] === 2)

count it as alive.

Both values represent cells that were alive in the original generation.

Step 3 — Apply State Transitions

For a live cell:

Live neighbors < 2
        ↓
Cell dies
Live neighbors = 2 or 3
        ↓
Cell survives
Live neighbors > 3
        ↓
Cell dies

For a dead cell:

Exactly 3 live neighbors
        ↓
Cell becomes alive
Step 4 — Use Temporary States

Instead of immediately converting:

1 → 0

store:

1 → 2

Instead of immediately converting:

0 → 1

store:

0 → -1

This preserves the original generation while processing the board.

Step 5 — Finalize the Board

After all cells have been processed:

2  →  0
-1 →  1

The board now represents the next generation.

🔍 Example
Input
[
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

During the first pass, some cells may temporarily become:

[
    [0, 2, 0],
    [-1, 0, 1],
    [1, 1, 1],
    [0, -1, 0]
]

Remember:

2  = alive → dead
-1 = dead → alive

After converting temporary states:

[
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0]
]
🧑‍💻 JavaScript Solution
/**
 * LeetCode 289 - Game of Life
 *
 * @param {number[][]} board
 * @return {void}
 * Do not return anything, modify board in-place instead.
 */
var gameOfLife = function (board) {
    const rows = board.length;
    const cols = board[0].length;


    // All possible directions around a cell
    const directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ];


    // Counts neighbors that were originally alive
    function countLiveNeighbors(row, col) {
        let liveNeighbors = 0;


        for (const [dr, dc] of directions) {
            const newRow = row + dr;
            const newCol = col + dc;


            // Ensure the neighbor is inside the board
            if (
                newRow >= 0 &&
                newRow < rows &&
                newCol >= 0 &&
                newCol < cols
            ) {
                // 1 = alive and remains alive
                // 2 = alive but will die
                if (
                    board[newRow][newCol] === 1 ||
                    board[newRow][newCol] === 2
                ) {
                    liveNeighbors++;
                }
            }
        }


        return liveNeighbors;
    }


    // First pass: determine transitions
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const liveNeighbors = countLiveNeighbors(row, col);


            // Originally alive
            if (board[row][col] === 1) {
                if (liveNeighbors < 2 || liveNeighbors > 3) {
                    // Alive -> Dead
                    board[row][col] = 2;
                }
            }


            // Originally dead
            else {
                if (liveNeighbors === 3) {
                    // Dead -> Alive
                    board[row][col] = -1;
                }
            }
        }
    }


    // Second pass: finalize transitions
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
📊 Complexity Analysis

Let:

m = number of rows
n = number of columns

Each cell checks at most eight neighbors.

Since eight is a constant:

Time Complexity
O(m × n)
Space Complexity
O(1)

No additional matrix or data structure proportional to the board size is created.

🔄 Approach Comparison
Approach	Time	Extra Space
Create a new board	O(m × n)	O(m × n)
Copy and update	O(m × n)	O(m × n)
In-place state encoding	O(m × n)	O(1)

The in-place approach is optimal in terms of auxiliary space.

⚠️ Common Mistakes
1. Updating Cells Immediately

This is incorrect:

if (shouldDie) {
    board[row][col] = 0;
}

The problem is that future cells may use this updated value when counting their neighbors.

The Game of Life requires all transitions to happen simultaneously.

The solution is:

Original State
      ↓
Temporary State
      ↓
Final State
2. Counting Newly Alive Cells

A cell marked:

-1

was originally dead.

Even though it will become alive, it must not be counted as a live neighbor during the first pass.

3. Forgetting Cells Marked as 2

A cell marked:

2

was originally alive.

Therefore, it must still be counted as a live neighbor.

if (cell === 1 || cell === 2)
4. Ignoring Board Boundaries

Cells near the edges have fewer than eight valid neighbors.

Always check:

newRow >= 0 &&
newRow < rows &&
newCol >= 0 &&
newCol < cols

before accessing a neighboring cell.

🚀 Implementation Highlights
Language: JavaScript ES6+
Technique: In-place state encoding
Category: Matrix Simulation
Traversal: Two-pass matrix traversal
Time Complexity: O(m × n)
Extra Space: O(1)
Key Challenge: Simultaneous state transitions
🧠 Lessons Learned
1. Preserve the Original State

When an algorithm requires simultaneous updates, modifying values immediately can destroy information needed later.

A useful strategy is to temporarily encode:

Old State + New State

inside the existing data structure.

2. Input Can Be Used as Temporary Storage

Instead of creating another matrix:

Original Board
+
New Board

we reuse the existing board.

This is a common technique in problems that require:

O(1) auxiliary space
3. Two-Pass Algorithms Are Useful for Simultaneous Updates

A common pattern is:

Pass 1
Determine and encode transitions
        ↓
Pass 2
Finalize transitions

This pattern appears in many in-place simulation and matrix problems.

4. Temporary Values Can Store State Transitions

Instead of thinking of a cell as having only:

Dead
Alive

we temporarily expand the possible states:

Dead → Dead
Alive → Alive
Alive → Dead
Dead → Alive

This makes it possible to remember both generations simultaneously.

🎯 Key Pattern
          ┌────────────────┐
          │ Original State │
          └───────┬────────┘
                  ↓
          ┌────────────────┐
          │ Encode Change  │
          └───────┬────────┘
                  ↓
          ┌────────────────┐
          │ Finalize State │
          └────────────────┘

When updates must happen simultaneously but extra space is restricted, encode both the old and new states directly inside the input.

🔗 Related Concepts
Matrix Simulation
In-Place Algorithms
State Encoding
Cellular Automata
Two-Pass Algorithms
Space Optimization
Grid Traversal
Neighbor Enumeration
🔗 Related LeetCode Problems
#	Problem	Difficulty	Main Concept
73	Set Matrix Zeroes	🟡 Medium	In-Place Markers
289	Game of Life	🟡 Medium	State Encoding
48	Rotate Image	🟡 Medium	In-Place Matrix
54	Spiral Matrix	🟡 Medium	Matrix Traversal
130	Surrounded Regions	🟡 Medium	Grid Traversal
200	Number of Islands	🟡 Medium	Matrix + DFS/BFS
🌍 Follow-Up: What About an Infinite Board?

The standard problem uses a finite 2D array, but the follow-up asks how an effectively infinite board could be handled when live cells reach the boundaries.

A practical approach would be to store only live cells in a sparse data structure, such as a Set or hash-based representation:

Set of live cell coordinates

For example:

"2,3"
"5,7"
"10,4"

Instead of storing an enormous grid:

1000000 × 1000000

we only store cells that are actually alive.

This is especially effective when the board is sparse.

📚 Reference

LeetCode — 289. Game of Life

The official problem defines the four transition rules, simultaneous updates, and the in-place follow-up.

📁 Recommended Repository Structure
LeetCode-Solutions/
│
├── medium/
│   └── matrix/
│       └── game-of-life/
│           ├── README.md
│           └── solution.js
│
├── notes/
│   ├── Patterns.md
│   ├── Complexity.md
│   ├── InPlaceAlgorithms.md
│   └── StateEncoding.md
│
└── README.md
<div align="center">
🧬 Problem #289

Difficulty: Medium
Language: JavaScript
Time Complexity: O(m × n)
Space Complexity: O(1)

🔑 Pattern

Read Original State → Encode Transition → Finalize State

⭐ Keep solving. Keep learning. Keep improving.

</div> ```