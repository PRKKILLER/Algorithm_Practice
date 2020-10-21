"""  
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as 
you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, 
it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return rooms
        
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        directions = [(-1,0), (0,1), (1,0),(0,-1)]
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        while q:
            sz = len(q)
            for idx in range(sz):
                i, j = q.popleft()
                for x, y in directions:
                    di, dj = i + x, j + y
                    if 0 <= di < m and 0 <= dj < n and rooms[di][dj] == INF:
                        rooms[di][dj] = rooms[i][j] + 1
                        q.append((di, dj))