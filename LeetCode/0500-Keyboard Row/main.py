"""  
Given an array of strings words, return the words that can be typed using letters of the alphabet on 
only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
"""


class Solution:
    # solution 1: using hashmap to mapping key to row
    # time complexity: o(N); space complexity: O(1)
    def findWords(self, words: List[str]) -> List[str]:
        d = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
             'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
             'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}

        res = []
        for w in words:
            word = w.lower()
            anchor = d[word[0]]
            for i in range(len(word)):
                if d[word[i]] != anchor:
                    break
                if i == len(word) - 1:
                    res.append(w)

        return res

    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = set('qwertyuiop'), set(
            'asdfghjkl'), set('zxcvbnm')
        res = []
        for word in words:
            w = set(word.lower())
            # check if w is the subset of any of the lines above
            if w <= line1 or w <= line2 or w <= line3:
                res.append(word)

        return res
