"""  
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().


Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
"""


class Solution:
    # time complexity: O(M*N)
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(haystack) < len(needle):
            return -1

        m, n, p = len(haystack), len(needle), 0
        while p + n <= m:
            for i in range(n):
                if haystack[p+i] != needle[i]:
                    break
                if i == n - 1:
                    return p
            p += 1

        return -1
