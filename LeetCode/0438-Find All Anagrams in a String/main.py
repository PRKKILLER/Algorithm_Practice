"""  
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        if m > n:
            return []

        dic = [0] * 26
        for c in p:
            dic[ord(c) - 97] += 1

        window = [0] * 26
        res = []
        for c in s[:m]:
            window[ord(c) - 97] += 1
        # array-wise compare takes O(26)-> O(1)
        if window == dic:
            res.append(0)

        lo = 0
        for hi in range(m, n):
            window[ord(s[lo]) - 97] -= 1
            window[ord(s[hi]) - 97] += 1
            lo += 1
            if window == dic:
                res.append(lo)

        return res
