"""  
Given two strings s1 and s2, return true if s2 contains the permutation of s1.

In other words, one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""

"""  
Important metric if two strings are anagram:
2 strings must have the same character frequencies.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        # install character's frequency
        dic = [0] * 26
        for c in s1:
            dic[ord(c) - 97] += 1

        tmp = [0] * 26
        for i in range(m):
            tmp[ord(s2[i]) - 97] += 1

        if tmp == dic:
            return True

        lo, hi = 0, m
        while hi < n:
            tmp[ord(s2[lo]) - 97] -= 1
            tmp[ord(s2[hi]) - 97] += 1
            if tmp == dic:
                return True
            lo += 1
            hi += 1

        return False
