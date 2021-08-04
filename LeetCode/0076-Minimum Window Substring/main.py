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
        m, n = len(s), len(t)
        min_len = m + 1
        lo = start = 0

        dic = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            dic[c] += 1

        match, cnt = len(dic), 0

        for i in range(m):
            if s[i] in dic:
                window[s[i]] += 1
                if window[s[i]] == dic[s[i]]:
                    cnt += 1

            while cnt == match:
                if (cur_len := i - lo + 1) < min_len:
                    min_len = cur_len
                    start = lo

                if s[lo] in dic:
                    window[s[lo]] -= 1
                    if window[s[lo]] < dic[s[lo]]:
                        cnt -= 1

                lo += 1

        return s[start:start + min_len] if min_len <= m else ''
