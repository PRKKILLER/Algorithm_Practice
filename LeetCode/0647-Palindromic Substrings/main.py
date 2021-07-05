"""  
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.


Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
"""


class Solution:
    # expend around possible centers
    # Time complexity: O(N^2); Space complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        def expend(lo, hi):
            ret = 0
            while 0 <= lo and hi < n and s[lo] == s[hi]:
                ret += 1
                lo -= 1
                hi += 1

            return ret

        for i in range(n):
            ans += expend(i, i)  # assume palindromic substr length is odd
            ans += expend(i, i + 1)  # assume palindromic substr length is even

        return ans

    # dynamic programming
    # Time complexity: O(N^2); Space complexity: O(N^2)
    """  
    dp[i][j] = True if substring[i : j] is palindromic else False

    => dp[i][j] = True if dp[i + 1][j - 1] == True and s[i] == s[j]
    """

    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        # dp[i][j] = True if substring[i : j] is palindromic else False
        dp = [[False] * n for _ in range(n)]
        ans = n

        # palindromic substrings with length == 1
        for i in range(n):
            dp[i][i] = True

        # palindromic substrings with length == 2
        for i in range(n - 1):
            dp[i][j] = True if s[i] == s[i + 1] else False
            ans += dp[i][j]

        # all other cases
        for l in range(3, n):
            for i in range(n - l + 1):
                j = i + j - 1
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                ans += dp[i][j]

        return ans
