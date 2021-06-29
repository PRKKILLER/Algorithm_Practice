"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
from collections import defaultdict


class Solution:
    # time complexity: O(2N)
    # using dict to memorize the occurrences of each character
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = hi = max_len = 0
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

    # time complexity: O(N)
    # using dict to memorize the position of last appearance of characters
    def lengthOfLongestSubstring2(self, s: str) -> int:
        encountered = {}
        anchor = res = 0

        for i, c in enumerate(s):
            if c in encountered and encountered[c] >= anchor:
                anchor = encountered[c] + 1  # jump to the next position
            else:
                res = max(res, i - anchor + 1)
            encountered[c] = i

        return res


if __name__ == '__main__':
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring2(s))
