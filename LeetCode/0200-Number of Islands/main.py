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
    # 基本思路：iterate each of the cell in the grid and if it is an island, do dfs,
    # mark all of its adjunct islands, cnt += 1
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        cnt = 0
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        
        return cnt
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] != '1':
            return
        grid[i][j] = '#' # mark as visited
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)