"""  
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        
        def backtrack(row, col, suffix):
            if len(suffix) == 0:
                return True
            
            if row < 0 or row == m or col < 0 or col == n or board[row][col] != suffix[0]:
                return False
            
            ret = False
            # mark the current choice before exploring further
            board[row][col] = '#'
            
            for x, y in directions:
                ret = backtrack(row + x, col + y, suffix[1:])
                # break immediately if find the valid answer
                # break instead of return to do some cleanup afterwards
                if ret: break
            
            board[row][col] = suffix[0]
            return ret
        
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, word):
                    return True
                
        return False