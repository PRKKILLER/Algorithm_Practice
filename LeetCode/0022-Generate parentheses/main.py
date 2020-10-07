"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    """ 
    一个合法的括号匹配组合有以下的性质:
    1. 左右括号的数量相等
    2. 对于一个「合法」的括号字符串组合 p，必然对于任何 0 <= i < len(p) 
    都有：子串 p[0..i] 中左括号的数量都大于或等于右括号的数量

    这一题可以套用回溯算法的思路，对于每个位置，有'('和')'两种放置方法
    然后检查放置括号后是否符合,再利用left和right两个变量当前子串左右括号的数量
    """
    def generateParenthesis(self, n: int):
        self.res = []
        self.backtrack('(', n, 1, 0)
        return self.res

    def backtrack(self, track, n, left, right):
        # track = track[:]

        if left < right:  # 若当前子串右括号数量 > 左括号，False
            return 
        if left > n or right > n: # 若当前左/右括号 > n， FALSE
            return 
        if left == n and right == n: # 若当前左右括号数量刚好=n
            self.res.append(track)
        
        # try '('
        track += '('
        self.backtrack(track, n, left+1, right)
        track = track[:-1] # backtrack

        # try ')'
        track += ')'
        self.backtrack(track, n, left, right+1)
        track = track[:-1] # backtrack

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))