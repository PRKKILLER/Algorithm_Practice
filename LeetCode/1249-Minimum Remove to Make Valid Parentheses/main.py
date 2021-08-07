"""  
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
"""

"""  
Key property of valid parentheses:
Every prefix of a valid parentheses string has a number of open parentheses greater or equal
than closed parentheses; similar pattern applys to closed parentheses if you traverse backwards.

Check the array from left to right, remove characters that do not meet the property mentioned above, 
same idea in backward way.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []

        # traverse from left to right
        lp_cnt = rp_cnt = 0  # cnt of left and right parenthesis
        for c in s:
            if c != ')':
                if c == '(':
                    lp_cnt += 1
                stk.append(c)
            else:
                if rp_cnt + 1 > lp_cnt:
                    pass
                else:
                    rp_cnt += 1
                    stk.append(')')

        res = []
        lp_cnt = rp_cnt = 0
        # traverse backwards
        while stk:
            c = stk.pop()
            if c != '(':
                if c == ')':
                    rp_cnt += 1
                res.append(c)
            else:
                if lp_cnt + 1 > rp_cnt:
                    pass
                else:
                    lp_cnt += 1
                    res.append('(')

        return ''.join(res[::-1])

    """  
    Use string builder + stack to get the final result:
    1. Identify all the indexes that should be removed
    2. Build new string with removed indexes

    If we meet open parentheses, we push it to stack; 
    if we meet close parentheses, if stack is empty, which means this close parentheses is invalid,
    add its index to "indexes_to_remove" set;
    After we traversed the whole string, if stack is not empty, which means there are invalid
    open parentheses that don't have matching close parentheses, add them to the "indexes_to_remove"
    set
    """

    def minRemoveToMakeValid2(self, s: str) -> str:
        indexes_to_remove = set()
        stk = []

        for idx, c in enumerate(s):
            if c == '(':
                stk.append(idx)
            elif c == ')':
                if not stk:
                    indexes_to_remove.add(idx)
                else:
                    stk.pop()

        # add invalid open parentheses' indexes to the "indexes_to_remove" set
        indexes_to_remove = indexes_to_remove.union(set(stk))
        res = []

        for idx, c in enumerate(s):
            if idx not in indexes_to_remove:
                res.append(c)

        return ''.join(res)
