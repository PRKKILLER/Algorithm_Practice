"""  
Given a string text, you want to use the characters of text to form as many instances of the word 
"balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances 
that can be formed.

Example:
Input: text = "nlaebolko"
Output: 1
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        mp = {'a': 1, 'b': 1, 'l': 2, 'n': 1, 'o': 2}
        counter = Counter(text)
        res = len(text)

        for k in mp:
            if k not in counter or counter[k] < mp[k]:
                return 0
            res = min(res, counter[k] // mp[k])

        return res
