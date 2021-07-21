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
        if not digits:
            return []

        mp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
              "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        n = len(digits)
        res = []

        def backtrack(idx: int, path: List[str]) -> None:
            if idx == n:
                res.append(''.join(path))
                return  # back to backtrack

            chars = mp[digits[idx]]
            for c in chars:
                # make decisions
                path.append(c)
                # move to next state
                backtrack(idx + 1, path)
                # backtrack
                path.pop()

        backtrack(0, [])
        return res
