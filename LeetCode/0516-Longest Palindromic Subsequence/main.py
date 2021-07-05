"""  
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements 
without changing the order of the remaining elements.


Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
"""


class Solution:
    """  
    dynamic programming
    dp[i][j] = longest palindromic subsequence in the range [i : j]
    i, j is the left and right boundary of the subsequence
    """

    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        dp = [[0 for _ in range(l)] for _ in range(l)]

        for i in range(l):
            dp[i][i] = 1

        # d is the distance between i, j
        for d in range(1, l):
            for i in range(l - d):
                j = i + d
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][l - 1]
