"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expend(lo, hi):
            while -1 < lo and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return s[lo+1:hi]

        res = ""
        for i in range(len(s)):
            odd = expend(i, i)
            even = expend(i, i+1)
            res = max(res, odd, even, key=len)

        return res


if __name__ == "__main__":
    sol = Solution()
    s = "sadfd"
    print(sol.longestPalindrome(s))
