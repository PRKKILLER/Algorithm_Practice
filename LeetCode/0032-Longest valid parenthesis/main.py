"""  
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.


Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """  
        dp[i] stores the longest valid parentheses ending at index i

        If s[i] is '(':
            set longest[i] to 0, because any string end with '(' cannot be a valid one.

        Else if s[i] is ')':

            If s[i-1] is '(':
                longest[i] = longest[i-2] + 2

            Else if s[i-1] is ')' and s[i-1-longest[i-1]] == '(': 
                longest[i] = longest[i-1] + 2 + longest[i-2-longest[i-1]]
        """
        if len(s) < 2:
            return 0

        res, n = 0, len(s)
        dp = [0] * n

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                else:
                    if i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == '(':
                        dp[i] = 2 + dp[i - 1]
                        if i - 2 - dp[i - 1] >= 0:
                            dp[i] += dp[i - 2 - dp[i - 1]]
                res = max(res, dp[i])

        return res
