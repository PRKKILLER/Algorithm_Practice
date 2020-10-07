"""  
The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.cnt = 0
        board = [['.'] * n for _ in range(self.n)]
        
        self.backtrack(board, 0)
        return self.cnt
    
    def backtrack(self, board, row):
        if row == self.n:
            self.cnt += 1
        
        for col in range(self.n):
            if self.isValid(board, row, col):
                board[row][col] = 'Q'
                self.backtrack(board, row + 1)
                board[row][col] = '.'
            
    def isValid(self, board, row, col):
        # check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
        # check top left part
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
            
        for i, j in zip(range(row-1, -1, -1), range(col+1, self.n)):
            if board[i][j] == 'Q':
                return False
            
        return True