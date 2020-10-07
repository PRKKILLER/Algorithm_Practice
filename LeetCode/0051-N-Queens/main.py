"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

a queen can attack any piece that is situated at the same row, column or diagonal of the queue.
"""

class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int):
        # initialize board
        # python 中 str是不可变对象，不能直接对其进行操作
        board = [['.'] * n for _ in range(n)]
        # start backtracing
        self.backtrack(board, 0, n)
        return self.res

    def backtrack(self, board, row, length):
        if row == length:
            self.res.append([''.join(board[i]) for i in range(length)])
            return
        
        for col in range(length):
            if not self.isValid(board, col, row, length):
                continue
            
            # make choice
            board[row][col] = 'Q'
            # move to next level decision tree
            self.backtrack(board, row+1, length)
            # remove current choice from board
            board[row][col] = '.'

    def isValid(self, board, col, row, length):
            # check row
            for i in range(length):
                if board[i][col] == 'Q':
                    return False
                
            # check top-right
            for i, j in zip(range(row-1, -1, -1), range(col+1, length)):
                if board[i][j] == 'Q':
                    return False

            # check top-left
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            return True

if __name__ == "__main__":
    # a = [['.'] * 4] * 4
    # a[0][0] = 'Q'
    # print(a)
    # print([''.join(a[i]) for i in range(4)])

    sol = Solution()
    sol.solveNQueens(4)
    for item in sol.res:
        print(item)

