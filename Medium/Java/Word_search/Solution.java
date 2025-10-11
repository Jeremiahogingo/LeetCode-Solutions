public class Solution {
    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;
        
        // Iterate through each cell in the grid
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                // Start DFS if first character matches
                if (dfs(board, word, row, col, 0)) {
                    return true;
                }
            }
        }
        return false; // Word not found
    }

    private boolean dfs(char[][] board, String word, int row, int col, int index) {
        // Check boundaries and character match
        if (row < 0 || row >= board.length || col < 0 || col >= board[0].length 
            || board[row][col] != word.charAt(index)) {
            return false;
        }

        // If all characters are matched
        if (index == word.length() - 1) {
            return true;
        }

        char temp = board[row][col]; // Store current character
        board[row][col] = '#'; // Mark as visited

        // Explore all four directions
        boolean found = dfs(board, word, row - 1, col, index + 1) ||
                        dfs(board, word, row + 1, col, index + 1) ||
                        dfs(board, word, row, col - 1, index + 1) ||
                        dfs(board, word, row, col + 1, index + 1);

        board[row][col] = temp; // Backtrack
        return found;
    }
}
