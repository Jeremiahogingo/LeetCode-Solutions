
/**
 * LeetCode 54 - Spiral Matrix
 *
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
    const result = [];

    let top = 0;
    let bottom = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {

        // 1. Traverse from left to right across the top row.
        for (let col = left; col <= right; col++) {
            result.push(matrix[top][col]);
        }
        top++;

        // 2. Traverse from top to bottom along the right column.
        for (let row = top; row <= bottom; row++) {
            result.push(matrix[row][right]);
        }
        right--;

        // 3. Traverse from right to left across the bottom row.
        if (top <= bottom) {
            for (let col = right; col >= left; col--) {
                result.push(matrix[bottom][col]);
            }
            bottom--;
        }

        // 4. Traverse from bottom to top along the left column.
        if (left <= right) {
            for (let row = bottom; row >= top; row--) {
                result.push(matrix[row][left]);
            }
            left++;
        }
    }

    return result;
};
