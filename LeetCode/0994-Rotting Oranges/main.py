"""  
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.
"""
from collections import deque

class Solution:
    """  
    该题是标准的bfs搜索题，但是难点在于同一时间，可能有多个rotten orange，
    而每个rotten orange都会向外辐射。因此一开始需要先把出事的rotten orange入队列
    并且利用标准的bfs解题框架，计算bfs的step
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        q = deque([])
        m, n = len(grid), len(grid[0])
        fresh_cnt = 0 # 新鲜水果计数

        # 初始的rotten oranges入队列
        for i in range(m):
            for j in range(n):
                if grid[m][n] == 1:
                    fresh_cnt += 1
                elif grid[m][n] == 2:
                    q.append((i, j))

        if fresh_cnt == 0: return 0

        offset = [(-1,0), (0,1), (1,0),(0,-1)]
        step = 0

        while q and fresh_cnt:
            step += 1
            sz = len(q)
            for i in range(sz):
                x, y = q.popleft()
                for item in offset:
                    a = x + item[0]
                    b = y + item[1]
                    if 0 <= a < m and 0 <= b < n and grid[a][b] == 1:
                        grid[a][b] = 2
                        q.append((a, b))
                        fresh_cnt -= 1
        
        return step if fresh_cnt == 0 else -1

