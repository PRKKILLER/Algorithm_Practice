"""  
In an alien language, surprisingly they also use english lowercase letters, 
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""


class Solution:
    """  
    time complexity: O(NlogN)
    """

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {c: chr(idx + 97) for idx, c in enumerate(order)}
        translate = []
        for w in words:
            translate.append(''.join(alphabet[c] for c in w))

        translate_sorted = sorted(translate)
        return translate == translate_sorted

    """  
    time complexity: O(NS)
    N: words list length; S: longest string length in words list
    """

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {c: idx for idx, c in enumerate(order)}
        translate = [[mapping[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(translate, translate[1:]))
