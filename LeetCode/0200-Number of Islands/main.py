""" 
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""


class Solution:
    """  
    DFS solution
    Time complexity : O(M×N) 
    Space complexity : worst case: O(MxN), in case grid is filled with lands
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(x: int, y: int) -> None:
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != '1':
                return
            grid[x][y] = '#'  # mark as visited
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    dfs(row, col)
                    res += 1

        return res

    """  
    BFS solution
    Time complexity: O(M x N)
    Space complexity: O(min(M, N))
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        m, n = len(grid), len(grid[0])
        res = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    res += 1
                    dq = deque([(row, col)])
                    grid[row][col] = '#'  # mark as visited
                    # traverse all its neighbors
                    while dq:
                        x, y = dq.popleft()
                        if x - 1 >= 0 and grid[x - 1][y] == '1':
                            grid[x - 1][y] = '#'
                            dq.append((x - 1, y))
                        if y - 1 >= 0 and grid[x][y - 1] == '1':
                            grid[x][y - 1] = '#'
                            dq.append((x, y - 1))
                        if x + 1 < m and grid[x + 1][y] == '1':
                            grid[x + 1][y] = '#'
                            dq.append((x + 1, y))
                        if y + 1 < n and grid[x][y + 1] == '1':
                            grid[x][y + 1] = '#'
                            dq.append((x, y + 1))

        return res
