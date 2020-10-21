"""  
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(prefix, cur):
            if len(cur) == 0:
                res.append(prefix)
                return
            
            d = mp[int(cur[0])]
            for w in d:
                prefix += w
                backtrack(prefix, cur[1:])
                prefix = prefix[:-1]
        
        if not digits: return []
        
        mp = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        res = []
        backtrack('', digits)
        return res

