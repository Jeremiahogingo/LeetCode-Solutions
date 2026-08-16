/**
 * @param {character[][]} board
 * @return {void}
 */
var solveSudoku = function (board) {

    const rows = Array.from({ length: 9 }, () => new Set());
    const cols = Array.from({ length: 9 }, () => new Set());
    const boxes = Array.from({ length: 9 }, () => new Set());

    const empty = [];

    // Initialize sets and collect empty cells
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {

            const value = board[r][c];

            if (value === ".") {
                empty.push([r, c]);
                continue;
            }

            const box = Math.floor(r / 3) * 3 + Math.floor(c / 3);

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

        const box = Math.floor(r / 3) * 3 + Math.floor(c / 3);

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