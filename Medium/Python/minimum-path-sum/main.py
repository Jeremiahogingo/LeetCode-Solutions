from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        # Fill first row
        for c in range(1, cols):
            grid[0][c] += grid[0][c - 1]

        # Fill first column
        for r in range(1, rows):
            grid[r][0] += grid[r - 1][0]

        # Fill remaining cells
        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[-1][-1]