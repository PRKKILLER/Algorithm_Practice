"""  
According to the Wikipedia's article: "The Game of Life, also known simply as Life, 
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 

using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. 
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: 
You cannot update some cells first and then use their updated values to update other cells.

2. In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches the border of the array. 
How would you address these problems?
"""

"""  
该题的难点在于所有cell的状态要同时进行更新，不能够先对某些cell的转态进行更新，然后用更新之后的状态去更新剩下的cell
而只用 0, 1这两个state是不可能做到的，因此需要增加2个state

DIE_NEXT = 3: 当前state=1，下一个state=0
LIVE_NEXT = 4: 当前state=0, 下一个state=1
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m, self.n = len(board), len(board[0])
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        self.DIE_NEXT = 2 # current: live -> next state: die
        self.LIVE_NEXT = 3 # current: die -> next state: live
        
        for i in range(self.m):
            for j in range(self.n):
                around = self.countLiveNeighbor(board, i, j)
                if board[i][j] == 0:
                    if around == 3:
                        board[i][j] = self.LIVE_NEXT
                else:
                    if around == 2 or around == 3:
                        continue
                    if around < 2 or around > 3:
                        board[i][j] = self.DIE_NEXT
        
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == self.DIE_NEXT:
                    board[i][j] = 0
                elif board[i][j] == self.LIVE_NEXT:
                    board[i][j] = 1
    
    
    def countLiveNeighbor(self, board, i, j):
        cnt = 0
        for x, y in self.directions:
            di, dj = i + x, j + y
            if 0 <= di < self.m and 0 <= dj < self.n:
                if board[di][dj] == 1 or board[di][dj] == self.DIE_NEXT:
                    cnt += 1
        
        return cnt