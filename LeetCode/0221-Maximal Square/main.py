"""  
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing 
only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

"""  
思路：dp: https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        max_side = 0
        
        # dp(i, j) represents the side length of the maximum square whose
        # bottom right corner is the cell with index (i, j) in the original matrix
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i][j], dp[i+1][j]) + 1
                    max_side = max(max_side, dp[i+1][j+1])
                    
        return max_side**2