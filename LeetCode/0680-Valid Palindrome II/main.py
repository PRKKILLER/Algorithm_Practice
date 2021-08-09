"""  
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
"""

"""  
We can use two pointers technique to solve this problem with O(N) time complexity.
We can initialize the lo and hi pointer to point to the front and end of the string
whenever we meet s[lo] != s[hi], we either delete s[lo] or delete s[hi],
and we compare "delete_lo == delete_lo[::-1]" or "delete_hi == delete_hi[::-1]"
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                delete_lo = s[:lo] + s[lo + 1:]
                delete_hi = s[:hi] + s[hi + 1:]
                return delete_lo == delete_lo[::-1] or delete_hi == delete_hi[::-1]
            lo += 1
            hi -= 1

        return True
