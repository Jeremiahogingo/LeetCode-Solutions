# 73. Set Matrix Zeroes

<div align="center">

![LeetCode](https://img.shields.io/badge/LeetCode-73-orange?style=for-the-badge\&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![Algorithm](https://img.shields.io/badge/Algorithm-In--Place%20Matrix-blue?style=for-the-badge)
![Space](https://img.shields.io/badge/Extra%20Space-O\(1\)-green?style=for-the-badge)

**In-place matrix transformation using the first row and first column as markers.**

[![LeetCode Problem](https://img.shields.io/badge/View%20Problem-LeetCode-orange?style=flat-square\&logo=leetcode)](https://leetcode.com/problems/set-matrix-zeroes/)

</div>

---

## 📖 Overview

**Set Matrix Zeroes** is a matrix manipulation problem that requires modifying a matrix based on the location of its zero-valued elements.

The main challenge is performing the transformation **in place** while using only constant extra space.

A straightforward solution would maintain separate arrays or sets to record which rows and columns contain zeroes. However, that requires **O(m + n)** additional memory.

The optimal solution takes advantage of the matrix itself by using its **first row and first column as marker storage**.

This allows us to achieve:

```text
Time Complexity:  O(m × n)
Space Complexity: O(1)
```

---

# 💡 Core Idea

Whenever we encounter a zero at:

```text
matrix[i][j]
```

we need to remember that:

```text
Row i    → must become zero
Column j → must become zero
```

Instead of creating separate storage, we use:

```text
matrix[i][0]
matrix[0][j]
```

as markers.

For example:

```text
1  2  3
4  0  6
7  8  9
```

The zero at `[1][1]` causes:

```text
matrix[1][0] = 0
matrix[0][1] = 0
```

The matrix now contains information telling us:

```text
Row 1    → zero
Column 1 → zero
```

We can then apply those markers after finishing the initial scan.

---

# 🧠 The Important Trick

There is one problem.

The first row and first column are themselves being used to store markers.

Therefore, if we encounter:

```text
matrix[0][j] === 0
```

we cannot immediately know whether:

* the zero originally existed there, or
* it was placed there as a marker.

The same applies to the first column.

Therefore, we separately track:

```javascript
let firstRowZero = false;
let firstColZero = false;
```

These variables preserve the original state of the first row and first column.

---

# 🔄 Algorithm

The algorithm can be divided into four phases.

### Phase 1 — Check the First Row

Scan the first row.

If any element is `0`:

```javascript
firstRowZero = true;
```

---

### Phase 2 — Check the First Column

Scan the first column.

If any element is `0`:

```javascript
firstColZero = true;
```

---

### Phase 3 — Create Markers

Ignore the first row and first column temporarily.

For every cell:

```javascript
matrix[i][j] === 0
```

mark:

```javascript
matrix[i][0] = 0;
matrix[0][j] = 0;
```

These markers identify which rows and columns need to be zeroed.

---

### Phase 4 — Apply the Markers

Process the remaining rows.

If:

```javascript
matrix[i][0] === 0
```

zero the entire row.

Then process the columns.

If:

```javascript
matrix[0][j] === 0
```

zero the entire column.

Finally, handle the first row and first column using:

```javascript
firstRowZero
firstColZero
```

---

# 🔍 Example

Consider:

```text
[
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
```

The zero occurs at:

```text
row = 1
column = 1
```

We use the first row and first column as markers:

```text
[
    [1, 0, 1],
    [0, 0, 1],
    [1, 1, 1]
]
```

The markers tell us:

```text
matrix[1][0] = 0
        ↓
Row 1 must become zero

matrix[0][1] = 0
        ↓
Column 1 must become zero
```

After applying the markers:

```text
[
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]
```

---

# ⚙️ Step-by-Step Implementation

## 1. Determine Matrix Dimensions

```javascript
const rows = matrix.length;
const cols = matrix[0].length;
```

---

## 2. Track the First Row

```javascript
let firstRowZero = false;

for (let j = 0; j < cols; j++) {
    if (matrix[0][j] === 0) {
        firstRowZero = true;
        break;
    }
}
```

---

## 3. Track the First Column

```javascript
let firstColZero = false;

for (let i = 0; i < rows; i++) {
    if (matrix[i][0] === 0) {
        firstColZero = true;
        break;
    }
}
```

---

## 4. Mark Rows and Columns

Start from `1` instead of `0` because the first row and column are reserved for markers.

```javascript
for (let i = 1; i < rows; i++) {
    for (let j = 1; j < cols; j++) {

        if (matrix[i][j] === 0) {
            matrix[i][0] = 0;
            matrix[0][j] = 0;
        }
    }
}
```

---

## 5. Zero Marked Rows

```javascript
for (let i = 1; i < rows; i++) {

    if (matrix[i][0] === 0) {

        for (let j = 1; j < cols; j++) {
            matrix[i][j] = 0;
        }
    }
}
```

---

## 6. Zero Marked Columns

```javascript
for (let j = 1; j < cols; j++) {

    if (matrix[0][j] === 0) {

        for (let i = 1; i < rows; i++) {
            matrix[i][j] = 0;
        }
    }
}
```

---

## 7. Handle the First Row

```javascript
if (firstRowZero) {

    for (let j = 0; j < cols; j++) {
        matrix[0][j] = 0;
    }
}
```

---

## 8. Handle the First Column

```javascript
if (firstColZero) {

    for (let i = 0; i < rows; i++) {
        matrix[i][0] = 0;
    }
}
```

---

# 🧑‍💻 JavaScript Solution

```javascript
/**
 * LeetCode 73 - Set Matrix Zeroes
 *
 * @param {number[][]} matrix
 * @return {void}
 * Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {

    const rows = matrix.length;
    const cols = matrix[0].length;

    // Track whether the first row originally contained a zero
    let firstRowZero = false;

    for (let j = 0; j < cols; j++) {
        if (matrix[0][j] === 0) {
            firstRowZero = true;
            break;
        }
    }

    // Track whether the first column originally contained a zero
    let firstColZero = false;

    for (let i = 0; i < rows; i++) {
        if (matrix[i][0] === 0) {
            firstColZero = true;
            break;
        }
    }

    // Use the first row and first column as markers
    for (let i = 1; i < rows; i++) {

        for (let j = 1; j < cols; j++) {

            if (matrix[i][j] === 0) {

                // Mark the row
                matrix[i][0] = 0;

                // Mark the column
                matrix[0][j] = 0;
            }
        }
    }

    // Zero all marked rows
    for (let i = 1; i < rows; i++) {

        if (matrix[i][0] === 0) {

            for (let j = 1; j < cols; j++) {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero all marked columns
    for (let j = 1; j < cols; j++) {

        if (matrix[0][j] === 0) {

            for (let i = 1; i < rows; i++) {
                matrix[i][j] = 0;
            }
        }
    }

    // Handle the first row
    if (firstRowZero) {

        for (let j = 0; j < cols; j++) {
            matrix[0][j] = 0;
        }
    }

    // Handle the first column
    if (firstColZero) {

        for (let i = 0; i < rows; i++) {
            matrix[i][0] = 0;
        }
    }
};
```

---

# ❌ Approaches That Use More Space

Understanding the alternatives makes the optimal solution easier to appreciate.

## Approach 1 — Create a Copy

Create another matrix and use it to determine which cells should become zero.

```text
Time:  O(m × n)
Space: O(m × n)
```

This is simple but inefficient in terms of memory.

---

## Approach 2 — Store Rows and Columns

Maintain two arrays:

```javascript
const zeroRows = [];
const zeroCols = [];
```

When a zero is found, record its row and column.

```text
Time:  O(m × n)
Space: O(m + n)
```

Better than copying the entire matrix, but still not optimal.

---

## Approach 3 — First Row/Column Markers

Use the input matrix itself to store the required information.

```text
Time:  O(m × n)
Space: O(1)
```

This is the optimal approach.

---

# 📊 Complexity Analysis

Let:

* `m` = number of rows
* `n` = number of columns

| Approach             |         Time | Extra Space |
| -------------------- | -----------: | ----------: |
| Matrix Copy          |     O(m × n) |    O(m × n) |
| Row/Column Arrays    |     O(m × n) |    O(m + n) |
| **In-Place Markers** | **O(m × n)** |    **O(1)** |

### Time Complexity

```text
O(m × n)
```

The matrix is traversed a constant number of times.

### Space Complexity

```text
O(1)
```

Only a few variables are used. No additional data structure grows with the matrix size.

---

# ⚠️ Common Mistakes

## 1. Zeroing Immediately

A common incorrect approach is:

```javascript
if (matrix[i][j] === 0) {
    zeroRow(i);
    zeroColumn(j);
}
```

This can create new zeroes that are mistaken for original zeroes.

The correct pattern is:

```text
Detect → Mark → Apply
```

---

## 2. Forgetting the First Row

The first row is used as marker storage, but it can also contain an original zero.

Always preserve its original state:

```javascript
let firstRowZero = false;
```

---

## 3. Forgetting the First Column

The same problem applies to the first column:

```javascript
let firstColZero = false;
```

---

## 4. Starting the Marker Scan at `0`

This can overwrite marker information.

The marker scan should begin at:

```javascript
i = 1
j = 1
```

---

# 🚀 Implementation Highlights

* **Language:** JavaScript ES6+
* **Technique:** In-place marker manipulation
* **Data Structure:** 2D Array
* **Traversal:** Matrix traversal
* **Extra Space:** O(1)
* **Time:** O(m × n)
* **Mutation:** Modifies the input matrix directly
* **Optimization:** Uses existing matrix cells as temporary storage

---

# 🧠 Lessons Learned

### 1. Use the Input as Storage When Appropriate

When a problem requires constant extra space, ask:

> Can I encode the information I need inside the existing input?

Here, the first row and column provide enough storage for the markers.

---

### 2. Separate Detection from Modification

A useful general pattern is:

```text
1. Detect
2. Record / Mark
3. Modify
```

This prevents changes made during processing from corrupting the information still needed by the algorithm.

---

### 3. Boundary Elements Often Need Special Handling

The first row and first column have two responsibilities:

```text
Original matrix data
+
Marker storage
```

Therefore, they cannot be treated exactly like the rest of the matrix.

---

### 4. Optimal Space Does Not Always Require More Time

The O(1)-space solution still maintains:

```text
O(m × n)
```

time complexity.

The optimization comes from **reusing existing memory**, not from reducing the number of cells processed.

---

# 🎯 Key Takeaway

The most important pattern from this problem is:

```text
             ┌──────────┐
             │  Detect  │
             └────┬─────┘
                  ↓
             ┌──────────┐
             │   Mark   │
             └────┬─────┘
                  ↓
             ┌──────────┐
             │  Apply   │
             └──────────┘
```

> **When an in-place problem asks you to remember information about rows or columns, consider using part of the input as marker storage.**

This technique is particularly useful for matrix and array problems where **O(1) auxiliary space** is required.

---

# 🔗 Related Concepts

* In-Place Algorithms
* Matrix Manipulation
* Two-Dimensional Arrays
* Array Traversal
* Space Optimization
* Marker Arrays
* Constant-Space Algorithms
* Boundary State Management

---

# 🔗 Related LeetCode Problems

|   # | Problem                                                       | Difficulty | Main Concept            |
| --: | ------------------------------------------------------------- | :--------: | ----------------------- |
|  36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)   |  🟡 Medium | Matrix + Hashing        |
|  48 | [Rotate Image](https://leetcode.com/problems/rotate-image/)   |  🟡 Medium | In-Place Matrix         |
|  54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) |  🟡 Medium | Matrix Traversal        |
|  73 | **Set Matrix Zeroes**                                         |  🟡 Medium | In-Place Markers        |
| 289 | [Game of Life](https://leetcode.com/problems/game-of-life/)   |  🟡 Medium | In-Place State Encoding |

---

# 📚 References

* **LeetCode:** [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
* **LeetCode Solutions:** [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/solutions/)

---

---

<div align="center">

### 🧩 Problem #73

**Difficulty:** Medium
**Language:** JavaScript
**Time Complexity:** O(m × n)
**Space Complexity:** O(1)

---

**Detect → Mark → Apply**

⭐ **Keep solving. Keep learning. Keep improving.**

</div>
