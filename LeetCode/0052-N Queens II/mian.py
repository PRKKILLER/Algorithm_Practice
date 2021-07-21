"""  
The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.res = 0

        def backtrack(row: int):
            if row == n:
                self.res += 1
                return

            for col in range(n):
                if is_valid(row, col):
                    # make decision
                    board[row][col] = 'Q'
                    # move to next row
                    backtrack(row + 1)
                    # backtrack
                    board[row][col] = '.'

        def is_valid(row: int, col: int):
            # check column
            for r in range(row):
                if board[r][col] == 'Q':
                    return False

            # check top left
            for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[r][c] == 'Q':
                    return False

            # check top right
            for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[r][c] == 'Q':
                    return False

            return True

        backtrack(0)
        return self.res
