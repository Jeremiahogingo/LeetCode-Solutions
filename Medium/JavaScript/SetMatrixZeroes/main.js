/**
 * @param {number[][]} matrix
 * @return {void}
 * Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {

    const rows = matrix.length;
    const cols = matrix[0].length;

    // Check whether the first row originally contains zero
    let firstRowZero = false;

    for (let j = 0; j < cols; j++) {
        if (matrix[0][j] === 0) {
            firstRowZero = true;
            break;
        }
    }

    // Check whether the first column originally contains zero
    let firstColZero = false;

    for (let i = 0; i < rows; i++) {
        if (matrix[i][0] === 0) {
            firstColZero = true;
            break;
        }
    }

    // Use first row and first column as markers
    for (let i = 1; i < rows; i++) {
        for (let j = 1; j < cols; j++) {

            if (matrix[i][j] === 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // Zero marked rows
    for (let i = 1; i < rows; i++) {

        if (matrix[i][0] === 0) {

            for (let j = 1; j < cols; j++) {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero marked columns
    for (let j = 1; j < cols; j++) {

        if (matrix[0][j] === 0) {

            for (let i = 1; i < rows; i++) {
                matrix[i][j] = 0;
            }
        }
    }

    // Handle first row
    if (firstRowZero) {
        for (let j = 0; j < cols; j++) {
            matrix[0][j] = 0;
        }
    }

    // Handle first column
    if (firstColZero) {
        for (let i = 0; i < rows; i++) {
            matrix[i][0] = 0;
        }
    }
};