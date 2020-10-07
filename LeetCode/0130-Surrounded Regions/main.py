
"""  
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board 
are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border 
will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or 
vertically.
"""
class Solution:
    """  
    思路：因为与边界上的’O‘相连通的区域的'O'不会被flip，只有不处在边界且不与边界相连通的'O'才会被flip
    因此首先从board的4个边界开始搜寻'O'的连通区域，把这些'O'排除在flip之外。
    然后再遍历board，将剩下的'O'进行flip
    此题仅需要对边界上的'O'进行dfs搜索
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        
        self.m, self.n = len(board), len(board[0])
        
        # 搜索上下边界
        for j in range(self.n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[self.m-1][j] == 'O':
                self.dfs(board, self.m-1, j)
        
        # 搜索左右边界
        for i in range(1, self.m-1):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][self.n-1] == 'O':
                self.dfs(board, i, self.n-1)
        
        # 进行flip
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
        

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or board[i][j] != 'O':
            return
        board[i][j] = '*'
        self.dfs(board, i-1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i+1, j)
        self.dfs(board, i, j-1)

