"""  
Given an array words of strings made only from lowercase letters, return a list of all characters 
that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, 
you need to include that character three times in the final answer.

You may return the answer in any order.


Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
"""


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = [0] * 26

        for c in words[0]:
            dic[ord(c) - 97] += 1

        for w in words[1:]:
            m = [0] * 26
            for c in w:
                m[ord(c) - 97] += 1

            for i in range(26):
                dic[i] = min(dic[i], m[i])

        res = []
        for i in range(26):
            if dic[i] > 0:
                res += [chr(i + 97)] * dic[i]

        return res
