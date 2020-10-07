"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.expend(s, i, i)  #假设palindrom长度为奇数
            even = self.expend(s, i, i+1)  #假设palindrom长度为偶数

            res = max(odd, even, res, key=len)
        return res
        
    def expend(self, s, lo, hi):
        # 跳出循环时，s[lo] != s[hi]
        # 因此 start = lo+1, end=hi-1
        while 0 <= lo and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return s[lo+1:hi] # 左闭右开

if __name__ == "__main__":
    sol = Solution()
    s = "sadfd"
    print(sol.longestPalindrome(s))

