"""  
Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to 
strings such that if each character in pattern is replaced by the string it maps to, 
then the resulting string is s. A bijective mapping means that no two characters map to the same string, 
and no character maps to two different strings.


Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
"""

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backtrack(pattern, s, memo):
            if len(pattern) == len(s) == 0:
                return True
            if len(pattern) == 0 or len(s) == 0:
                return False

            """
            When we find the match for pattern[0], we have len(pattern) - 1 letters left to match, 
            therefore the maximum length of pattern[0] can only be len(str) - (len(pattern) - 1) = len(str) - len(pattern) + 1. 
            For slicing in Python, that would make the upper-bound len(str) - len(pattern) + 2.
            """
            for end in range(1, len(s)-len(pattern)+2):
                p, w = pattern[0], s[:end]
                if p not in memo and w not in memo.values():
                    memo[p] = w
                    if backtrack(pattern[1:], s[end:], memo):
                        return True
                elif p in memo and w == memo[p]:
                    if backtrack(pattern[1:], s[end:], memo):
                        return True

            return False

        return backtrack(pattern, s, {})