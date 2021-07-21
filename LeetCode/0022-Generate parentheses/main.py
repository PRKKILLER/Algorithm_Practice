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
    def generateParenthesis(self, n: int) -> List[str]:
        """ 
    一个合法的括号匹配组合有以下的性质:
    1. 左右括号的数量相等
    2. 对于一个「合法」的括号字符串组合 p，必然对于任何 0 <= i < len(p) 
    都有：子串 p[0..i] 中左括号的数量都大于或等于右括号的数量

    这一题可以套用回溯算法的思路，对于每个位置，有'('和')'两种放置方法
    然后检查放置括号后是否符合,再利用left和right两个变量当前子串左右括号的数量
    """
        def backtrack(left: int, right: int, path: List[str]) -> None:
            if left < right:
                return
            if left > n:
                return
            if left == n and right == n:
                res.append(''.join(path))

            # try '('
            path.append('(')
            backtrack(left + 1, right, path)
            path.pop()

            # try ')'
            path.append(')')
            backtrack(left, right + 1, path)
            path.pop()

        res = []
        backtrack(1, 0, ['('])
        return res
