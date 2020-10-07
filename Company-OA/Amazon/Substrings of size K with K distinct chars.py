"""  
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
"""
from typing import List


"""  
思路：利用滑动窗口
"""
def substrings(s: str, k: int) -> List[str]:
    if not s or k == 0: return []

    res = set()
    m = {}
    start = 0
    for i in range(len(s)):
        if s[i] in m and m[s[i]] >= start:
            start = m[s[i]] + 1
        m[s[i]] = i
        if i - start + 1 == k:
            res.add(s[start : i+1])
            start += 1

    return list(res)


