"""  
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

把拥有相同字母的不同单词组合起来

时间复杂度: O(NKlogK)
N is the length of the str, and K is the maximum length of a string in strs
"""
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            # example: sorted('eat') = ['a', 'e', 't']
            chs = tuple(sorted(s))
            d[chs].append(s)

        return d.values()

    # use frequency to group anagrams
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            frequency = [0] * 26
            for c in s:
                frequency[ord(c) - 97] += 1

            d[tuple(frequency)].append(s)

        return d.values()

# Solution 2 using unique prime multiplication


class Solution2:
    def __init__(self):
        self._primes = {'a': 2,
                        'b': 3,
                        'c': 5,
                        'd': 7,
                        'e': 11,
                        'f': 13,
                        'g': 17,
                        'h': 19,
                        'i': 23,
                        'j': 29,
                        'k': 31,
                        'l': 37,
                        'm': 41,
                        'n': 43,
                        'o': 47,
                        'p': 53,
                        'q': 59,
                        'r': 61,
                        's': 67,
                        't': 71,
                        'u': 73,
                        'v': 79,
                        'w': 83,
                        'x': 89,
                        'y': 97,
                        'z': 101
                        }

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            product = 1
            for c in s:
                product *= self._primes[c]
            dic[product].append(s)

        return s.values()
