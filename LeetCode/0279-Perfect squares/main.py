"""
Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

class Solution:
    """  
    思路：动态规划
    对于任何一个数 a = some_number + j * j
    维护一个一维dp数组，dp[i] = 最小全平方和
    j ∈ [1, int(i**0.5)+1]
    """
    def numSquares(self, n: int) -> int:
        if n < 2: return n
        
        dp  = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        
        return dp[n]

    def numSquares2(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        for i in range(1, n+1):
            dp[i] = min(dp[i-j**2] for j in range(1, int(i**0.5) + 1)) + 1

        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    res = sol.numSquares(12)