# 54. Spiral Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-JavaScript-yellow)
![Topic](https://img.shields.io/badge/Topic-Array%20%7C%20Matrix-blue)
![Technique](https://img.shields.io/badge/Technique-Boundary%20Traversal-purple)

## Problem

**[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/)**

Given an `m × n` matrix, return all elements of the matrix in spiral order.

Spiral order means traversing the matrix clockwise, starting from the top-left element and moving through:

1. Left to right across the top row.
2. Top to bottom along the right column.
3. Right to left across the bottom row.
4. Bottom to top along the left column.

Repeat this process while unvisited elements remain.

## Approach: Boundary Traversal

The solution uses four boundary pointers to track the unvisited region of the matrix.

### Boundary Variables

| Variable | Purpose |
|---|---|
| `top` | First unvisited row |
| `bottom` | Last unvisited row |
| `left` | First unvisited column |
| `right` | Last unvisited column |

Initially:

```javascript
top = 0;
bottom = matrix.length - 1;
left = 0;
right = matrix[0].length - 1;
```

### Algorithm

While the unvisited region remains (`top <= bottom` and `left <= right`), perform four directional traversals.

**1. Traverse Left to Right**

- Visit every element in the current top row.
- Add each element to the result.
- Increment `top` to exclude the visited row.

**2. Traverse Top to Bottom**

- Visit every element in the current right column.
- Add each element to the result.
- Decrement `right` to exclude the visited column.

**3. Traverse Right to Left**

- Check whether an unvisited row remains.
- Visit every element in the current bottom row in reverse order.
- Decrement `bottom`.

**4. Traverse Bottom to Top**

- Check whether an unvisited column remains.
- Visit every element in the current left column in reverse order.
- Increment `left`.

The boundary checks prevent duplicate traversal when the remaining region contains only one row or one column.

## JavaScript Solution

```javascript
/**
 * LeetCode 54 - Spiral Matrix
 *
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
    if (!matrix.length || !matrix[0].length) return [];

    const result = [];

    let top = 0;
    let bottom = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {

        // 1. Traverse from left to right.
        for (let col = left; col <= right; col++) {
            result.push(matrix[top][col]);
        }
        top++;

        // 2. Traverse from top to bottom.
        for (let row = top; row <= bottom; row++) {
            result.push(matrix[row][right]);
        }
        right--;

        // 3. Traverse from right to left.
        if (top <= bottom) {
            for (let col = right; col >= left; col--) {
                result.push(matrix[bottom][col]);
            }
            bottom--;
        }

        // 4. Traverse from bottom to top.
        if (left <= right) {
            for (let row = bottom; row >= top; row--) {
                result.push(matrix[row][left]);
            }
            left++;
        }
    }

    return result;
};
```

## Example and Dry Run

### Example 1

**Input:**

```javascript
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
```

**Traversal:**

<pre>
1 → 2 → 3
        ↓
4   5   6
↑       ↓
7 ← 8 ← 9
</pre>

**Output:**

```javascript
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

**Explanation:**

- First row: `[1, 2, 3]`
- Right column: `[6, 9]`
- Bottom row: `[8, 7]`
- Left column: `[4]`
- Remaining inner element: `[5]`

Combining the elements produces the spiral traversal.

### Example 2

**Input:**

```javascript
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
];
```

**Output:**

```javascript
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

**Explanation:**

The traversal proceeds clockwise:

- Top row: `1, 2, 3, 4`
- Right column: `8, 12`
- Bottom row: `11, 10, 9`
- Left column: `5`
- Remaining inner row: `6, 7`

### Example 3: Single Row

**Input:**

```javascript
matrix = [[1, 2, 3, 4]];
```

**Output:**

```javascript
[1, 2, 3, 4]
```

The algorithm traverses the single row without attempting to revisit it.

### Example 4: Single Column

**Input:**

```javascript
matrix = [
    [1],
    [2],
    [3]
];
```

**Output:**

```javascript
[1, 2, 3]
```

The boundary conditions prevent duplicate elements when only one column remains.

## Complexity Analysis

Let:

- `m` represent the number of rows.
- `n` represent the number of columns.

| Complexity | Analysis |
|---|---|
| Time | `O(m × n)` |
| Auxiliary Space | `O(1)` excluding the output array |
| Output Space | `O(m × n)` |

**Time Complexity: `O(m × n)`**

Every matrix element is visited and added to the result exactly once. Therefore, the total traversal time is proportional to the number of matrix elements.

**Auxiliary Space Complexity: `O(1)`**

The algorithm uses only four boundary pointers and a fixed amount of additional memory.

The result array requires `O(m × n)` space, but it is excluded from auxiliary space complexity.

## Important Edge Cases

| Scenario | Expected Behavior |
|---|---|
| Single row | Traverse from left to right |
| Single column | Traverse from top to bottom |
| Square matrix | Complete clockwise spiral traversal |
| Rectangular matrix | Adjust boundaries after each direction |
| One remaining element | Add the element exactly once |
| Empty matrix | Return an empty array |

## Common Mistakes

**1. Forgetting to Update Boundaries**

After traversing a row or column, its boundary must move inward. Otherwise, previously visited elements may be included again.

**2. Missing Conditional Checks**

Before traversing the bottom row, check `top <= bottom`.

Before traversing the left column, check `left <= right`.

These checks prevent duplicate traversal in narrow remaining regions.

**3. Incorrect Loop Conditions**

Use inclusive comparisons (`<=` and `>=`) because both current boundaries are part of the unvisited region.

**4. Confusing Rows and Columns**

Remember:

- `matrix[row][col]` accesses an element.
- `matrix.length` gives the number of rows.
- `matrix[0].length` gives the number of columns.

## Key Takeaways

- Boundary pointers simplify two-dimensional matrix traversal.
- Four directional passes produce clockwise spiral order.
- Updating boundaries removes visited rows and columns.
- Conditional checks prevent duplicate elements.
- Each element is processed exactly once.
- The technique achieves linear time relative to the matrix size.

## Related Problems

| Problem | Difficulty | Main Concept |
|---|---|---|
| [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | In-Place Matrix Manipulation |
| [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | Boundary Traversal |
| [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | Medium | Matrix Construction |
| [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | In-Place Matrix |
| [289. Game of Life](https://leetcode.com/problems/game-of-life/) | Medium | Matrix Simulation |

## Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── JavaScript/
        ├── 54_Spiral_Matrix.js
        └── README.md
```

## References

- [LeetCode – Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [JavaScript Array Documentation – MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

---

**Problem:** 54  
**Difficulty:** Medium  
**Language:** JavaScript  
**Topics:** Array, Matrix, Simulation, Boundary Traversal  
**Time Complexity:** `O(m × n)`  
**Auxiliary Space:** `O(1)` excluding output

