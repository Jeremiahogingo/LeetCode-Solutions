class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = set()
        positive_diagonals = set()  # row + col
        negative_diagonals = set()  # row - col

        def backtrack(row: int) -> int:
            # A queen has been successfully placed in every row.
            if row == n:
                return 1

            solutions = 0

            for col in range(n):
                # Check column and both diagonals.
                if (
                    col in columns
                    or (row + col) in positive_diagonals
                    or (row - col) in negative_diagonals
                ):
                    continue

                # Place queen.
                columns.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)

                # Explore the next row.
                solutions += backtrack(row + 1)

                # Backtrack.
                columns.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)

            return solutions

        return backtrack(0)