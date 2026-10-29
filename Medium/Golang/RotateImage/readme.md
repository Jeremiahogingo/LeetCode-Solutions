# LeetCode 48: Rotate Image

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange)
![Language](https://img.shields.io/badge/Language-Go-00ADD8?logo=go&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Matrix-blue)

## Problem Description

Given an `n × n` square matrix representing an image, rotate the image **90 degrees clockwise in place**.

Modify the input matrix directly without allocating another matrix for the rotation.

**Problem link:** [LeetCode 48 — Rotate Image](https://leetcode.com/problems/rotate-image/description/)

## Approach: Transpose and Reverse

The rotation can be performed in two steps:

1. **Transpose the matrix:** Swap `matrix[i][j]` with `matrix[j][i]` across the main diagonal.
2. **Reverse each row:** Reverse the elements in every row to complete the clockwise rotation.

This approach modifies the original matrix and uses constant auxiliary space.

## Go Solution

```go
func rotate(matrix [][]int) {
    n := len(matrix)

    // Step 1: Transpose the matrix.
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            matrix[i][j], matrix[j][i] =
                matrix[j][i], matrix[i][j]
        }
    }

    // Step 2: Reverse each row.
    for i := 0; i < n; i++ {
        for left, right := 0, n-1; left < right; left, right = left+1, right-1 {
            matrix[i][left], matrix[i][right] =
                matrix[i][right], matrix[i][left]
        }
    }
}
```

## Examples

**Example 1**

Input:

```text
[[1,2,3],
 [4,5,6],
 [7,8,9]]
```

Output:

```text
[[7,4,1],
 [8,5,2],
 [9,6,3]]
```

**Example 2**

Input:

```text
[[5,1,9,11],
 [2,4,8,10],
 [13,3,6,7],
 [15,14,12,16]]
```

Output:

```text
[[15,13,2,5],
 [14,3,4,1],
 [12,6,8,9],
 [16,7,10,11]]
```

## Complexity Analysis

Let \(n\) be the number of rows or columns.

- **Time Complexity:** \(O(n^2)\) — transposing and reversing the matrix process a total of \(O(n^2)\) elements.
- **Auxiliary Space Complexity:** \(O(1)\) — the rotation is performed in place using a constant number of variables.

## Key Takeaways

- A clockwise 90-degree rotation can be achieved through transposition followed by row reversal.
- Transposition swaps rows and columns across the main diagonal.
- Reversing each row places the elements in their correct clockwise positions.
- In-place operations avoid allocating a second matrix.

## Related Problems

These problems reinforce matrix traversal, in-place modification, and array rotation.

| Problem | Difficulty | Connection |
|---|---|---|
| [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | Traverse a matrix in spiral order. |
| [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | Medium | Construct a matrix using directional traversal. |
| [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | Modify a matrix in place while managing row and column relationships. |
| [189. Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | Rotate an array using reversal techniques. |
| [289. Game of Life](https://leetcode.com/problems/game-of-life/) | Medium | Update a matrix in place under specific rules. |

## Repository Structure

```text
LeetCode-Solutions/
└── Medium/
    └── Golang/
        ├── 48_Rotate_Image.go
        └── README.md
```

## References

- [LeetCode Problem 48](https://leetcode.com/problems/rotate-image/description/)
- [Go Documentation](https://go.dev/doc/)
