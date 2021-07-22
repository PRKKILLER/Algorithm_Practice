"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(row: int, col: int) -> bool:
            if col == 9:
                return backtrack(row + 1, 0)
            if row == 9:
                return True

            if board[row][col] != '.':
                return backtrack(row, col + 1)

            for n in range(1, 10):
                num = str(n)
                if is_valid(row, col, num):
                    # make decision
                    board[row][col] = num
                    # move to the next state
                    # return if find valid
                    if backtrack(row, col + 1):
                        return True
                    board[row][col] = '.'

            return False  # 遍历了 1 ~ 9，没有匹配的

        def is_valid(row: int, col: int, num: str) -> bool:
            for i in range(9):
                # check row
                if board[row][i] == num:
                    return False
                # check col
                if board[i][col] == num:
                    return False

            # check 3 * 3 sub-grid
            row_bound = row // 3 * 3
            col_bound = col // 3 * 3

            for r in range(row_bound, row_bound + 3):
                for c in range(col_bound, col_bound + 3):
                    if board[r][c] == num:
                        return False

            return True
