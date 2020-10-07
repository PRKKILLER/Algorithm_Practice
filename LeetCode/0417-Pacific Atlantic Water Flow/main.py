"""  
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, 
the "Pacific ocean" touches the left and top edges of the matrix 
and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height 
equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.


Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

"""  
注意：题目问的是可以向pacific 和 atlantic 同时流水的位置
"""


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        
        m, n = len(matrix), len(matrix[0])
        directions = [(0,-1), (1,0), (0,1), (-1,0)]
        
        """  
        maintain two boolean matrix for two oceans, 
        indicating whether the point's water can reach to the ocean or not.
        """
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        
        def dfs(i, j, height, visited):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or matrix[i][j] < height:
                return
            
            visited[i][j] = True
            for x, y in directions:
                dfs(i+x, j+y, matrix[i][j], visited)
                
        for i in range(m):
            dfs(i, 0, float('-inf'), pacific)
            dfs(i, n-1, float('-inf'), atlantic)
            
        for j in range(n):
            dfs(0, j, float('-inf'), pacific)
            dfs(m-1, j, float('-inf'), atlantic)
            
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res