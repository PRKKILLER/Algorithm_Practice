"""  
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]

    """  
    利用排列组合定理
    因为robot只能向下或者向右走动，因此从左上角(1,1)走到终点(m,n)
    总共要走: m+n-2 向下走 m-1 歩，向右走 n-1 歩
    因此总的unique paths数量就是从m+n-2歩中取出m-1歩的方法的总数量
    """
    def uniquePaths2(self, m: int,  n: int) -> int:
        N = m + n - 2
        k = m - 1

        res = 1
        divisor = 1
        """  
        here we calculate the total possible path number
        Combination(N, k) = n! / (k!(n - k)!)
        reduce the numerator and denominator and get
        C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!
        """
        for i in range(1, k+1):
            res *= (N - k + i)
            divisor *= i

        return res // divisor