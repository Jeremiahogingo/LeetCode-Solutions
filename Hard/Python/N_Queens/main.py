from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        # Create an empty chessboard.
        board = [["."] * n for _ in range(n)]

        # Track occupied columns and diagonals.
        columns = set()
        positive_diagonals = set()  # row + col
        negative_diagonals = set()  # row - col

        def backtrack(row: int) -> None:
            # All queens have been successfully placed.
            if row == n:
                result.append(
                    ["".join(row) for row in board]
                )
                return

            # Try every column in the current row.
            for col in range(n):

                # Check whether the position is attacked.
                if (
                    col in columns
                    or (row + col) in positive_diagonals
                    or (row - col) in negative_diagonals
                ):
                    continue

                # Place the queen.
                board[row][col] = "Q"
                columns.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)

                # Move to the next row.
                backtrack(row + 1)

                # Undo the placement.
                board[row][col] = "."
                columns.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)

        backtrack(0)

        return result