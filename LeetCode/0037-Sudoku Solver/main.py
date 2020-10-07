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
        self.backtrack(board, 0, 0)

        
    def backtrack(self, board, i, j):
        if j == 9:
            return self.backtrack(board, i+1, 0)
        
        if i == 9:
            return True
        
        if board[i][j] != '.':
            return self.backtrack(board, i, j+1)
        
        for num in range(1, 10):
            num = str(num)
            if not self.is_valid(board, i, j, num):
                continue
            
            board[i][j] = num
            # 找到1个可行的解，理解结束递归
            if self.backtrack(board, i, j+1):
                return True
            board[i][j] = '.'
        
        # 穷举完1 - 9，依然没有有效解，此路不通
        return False

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[i][col] == num: # 检查列
                return False
            if board[row][i] == num: # 检查行
                return False
        
        top_row = row // 3 * 3
        top_col = col // 3 * 3
        for i in range(top_row, top_row+3):
            for j in range(top_col, top_col+3):
                if board[i][j] == num:
                    return False
        
        return True

