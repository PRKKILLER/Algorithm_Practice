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
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strs:
            # example: sorted('eat') = ['a', 'e', 't']
            chs = tuple(sorted(w))
            d[chs] += [w]
            
        return list(d.values())

    # use frequency to group anagrams
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            frequency = [0] * 26
            for c in s:
                frequency[ord(c) - 97] += 1
            
            d[tuple(frequency)].append(s)
        
        return list(d.values())