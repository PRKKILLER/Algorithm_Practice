"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo, hi = 0, 0
        max_len = 0
        d = defaultdict(int)
        
        while hi < len(s):
            c = s[hi]
            hi += 1
            d[c] += 1
            while d[c] > 1:
                c2 = s[lo]
                d[c2] -= 1
                lo += 1
            
            max_len = max(max_len, hi - lo)
            
        return max_len

