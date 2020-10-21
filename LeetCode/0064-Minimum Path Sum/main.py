"""  
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

"""  
思路：动态规划: grid[i][j] = minimize cost to get to the position (i,j)
首先要初始化 grid的 上 和 左 边界
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        
        m, n = len(grid), len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
            
        if m == 1: return grid[0][n-1]
        if n == 1: return grid[m-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                
        return grid[m-1][n-1]