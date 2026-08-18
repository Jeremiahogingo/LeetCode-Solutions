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

    // All 8 possible directions around a cell
    const directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ];

    // Count the number of originally live neighbors
    function countLiveNeighbors(row, col) {
        let liveNeighbors = 0;

        for (const [dr, dc] of directions) {
            const newRow = row + dr;
            const newCol = col + dc;

            // Check boundaries
            if (
                newRow >= 0 &&
                newRow < rows &&
                newCol >= 0 &&
                newCol < cols
            ) {
                // 1 = originally alive, still alive
                // 2 = originally alive, will die
                if (board[newRow][newCol] === 1 || board[newRow][newCol] === 2) {
                    liveNeighbors++;
                }
            }
        }

        return liveNeighbors;
    }

    // First pass:
    // Determine the next state while preserving the original state.
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const liveNeighbors = countLiveNeighbors(row, col);

            // Live cell dies
            if (board[row][col] === 1) {
                if (liveNeighbors < 2 || liveNeighbors > 3) {
                    // 1 -> 0
                    // Mark as 2 to remember it was originally alive
                    board[row][col] = 2;
                }
            }

            // Dead cell becomes alive
            else {
                if (liveNeighbors === 3) {
                    // 0 -> 1
                    // Mark as -1 to remember it was originally dead
                    board[row][col] = -1;
                }
            }
        }
    }

    // Second pass:
    // Convert temporary states to final states.
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