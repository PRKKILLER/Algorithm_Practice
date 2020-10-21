"""  
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        
        m, n = len(matrix), len(matrix[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # cache[i][j] 保存的是以 (i, j) 为起点的longest_increasing path 长度
        cache = [[-1] * n for _ in range(m)]
        
        def dfs(i, j, val):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= val: 
                return 0
            
            if cache[i][j] != -1: 
                return cache[i][j]
            
            res = 1
            
            for x, y in directions:
                di, dj = i + x, j + y
                cur_len = 1 + dfs(di, dj, matrix[i][j])
                res = max(res, cur_len)
            
            cache[i][j] = res
            return res
        
        ret = 0
        for i in range(m):
            for j in range(n):
                cur_len = dfs(i, j, float('-inf'))
                ret = max(ret, cur_len)
        
        return ret