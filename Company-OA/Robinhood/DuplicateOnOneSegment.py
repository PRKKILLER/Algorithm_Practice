"""  
Given an array of integers, count the number of contiguous subarrays, such that each element of the subarray 
appears at least twice

Example:
arr=[0,0,0], output: 3
There are 3 subarrays satisfy the criteria of containing only duplicate elements:
[0,0],[0,0],[0,0,0]

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""

from  collections import defaultdict
from typing import List

def solution2(arr: List[int]) -> int:
    if len(arr) < 2: return 0

    res = 0
    for h in range(1, 11):
        res = max(res, lsForUniqueChar(arr, h))
    
    return res

def lsForUniqueChar(arr, h):
    count = defaultdict(int)
    unique = 0
    no_less_than_2 = 0
    start = 0
    res = 0

    for i, c in enumerate(arr):
        count[c] += 1
        if count[c] == 1:
            unique += 1
        if count[c] == 2:
            no_less_than_2 += 1
        while start <= i and unique > h:
            if count[arr[start]] == 1:
                unique -= 1
            if count[arr[start]] == 2:
                no_less_than_2 -= 1
            count[arr[start]] -= 1
            start += 1
        if unique == h and no_less_than_2 == h:
            res = max(res, i - start + 1)
    
    return res

# Time complexity: O(n^2)
def solution(arr: List[int]) -> int:
    res = 0
    for i in range(len(arr)):
        counter = 0
        m = defaultdict(int)
        for j in range(i, len(arr)):
            m[arr[j]] += 1
            if m[arr[j]] == 2:
                counter += 1
            if counter and counter == len(m):
                res += 1

    return res

arr = [0,1,0,1,1,2]
print(solution2(arr))