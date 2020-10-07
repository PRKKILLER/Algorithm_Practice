"""  
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example1 :
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        if len(s) % 2: return False
        
        left = '([{'
        right = ')]}'
        stk = []
        for p in s:
            if p in left:
                stk.append(p)
            else:
                if not stk: return False
                l_idx = left.find(stk[-1])
                r_idx = right.find(p)
                if l_idx != r_idx: return False
                stk.pop()
        return not stk