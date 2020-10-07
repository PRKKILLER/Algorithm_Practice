"""  
Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be
only one unique minimum window in S.
"""

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 记录最短子串的起始位置和长度
        start, min_len = 0, float('inf')
        # 滑动窗口的左右指针
        lo, hi = 0, 0
        
        d = defaultdict(int)
        window = defaultdict(int)

        # 保存 target string 中各个字符出现的个数
        for c in t:
            d[c] += 1

        match = 0 # 当期子串匹配的字符数

        while hi < len(s):
            c1 = s[hi]
            hi += 1
            if c1 in d:
                window[c1] += 1
                if window[c1] == d[c1]:
                    match += 1
            
            # 若当前子串已满足条件，则开始移动左指针，收缩sliding window的size
            while match == len(d):
                if hi - lo < min_len:
                    start = lo
                    min_len = hi - lo

                # 移动左指针
                c2 = s[lo]
                if c2 in d:
                    window[c2] -= 1
                    if window[c2] < d[c2]:
                        match -= 1
                lo += 1

        return s[start:start+min_len] if min_len < float('inf') else ''
