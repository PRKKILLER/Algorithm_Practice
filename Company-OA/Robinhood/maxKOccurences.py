"""  
Given a string sequence and an array of strings words, find the maximal value of k for each element, 
such that words[i] is a k-occurrence of sequence.
Return the k-values as an array of integers of length words.length

Example:
words = ["ab","babc","bca"]
sequence = "ababcbabc"

Output: out=[2,2,0]
"""
from typing import List

def solution(sequence: str, words: List[str]) -> List[int]:
    res = []
    l = len(sequence)
    for w in words:
        n = len(w)
        start = sequence.find(w)
        if start == -1: 
            res.append(0)
        else:
            cnt = 1
            while start + n * (cnt+1) <= l:
                if sequence[start:start + n * (cnt+1)] == w * (cnt + 1):
                    cnt += 1
                else:
                    break
            res.append(cnt)

    return res

words = ["ab","babc","bca"]
sequence = "ababcbabc"
print(solution(sequence, words))