"""  
Given a string s, return the last substring of s in lexicographical order.

Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. 
The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"
"""

class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i+k] == s[j+k]:
                k += 1
            elif s[i+k] < s[j+k]:
                i = j
                j += 1
                k = 0
            else:
                j += k + 1
                k = 0
        return s[i:]

sol = Solution()
print(sol.lastSubstring("cacacb"))