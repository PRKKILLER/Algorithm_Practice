"""  
You are given an array of non-negative integers a. Fin how many elements of a have an odd number of occurrences
of the digit 0

Example:
a=[20,11,10,10070,7]
return: 3 (20,10,10070)
"""

from collections import Counter

def solution(arr):
    res = 0
    for num in arr:
        tmp = list(str(num))
        count = Counter(tmp)
        if count['0'] % 2:
            res += 1

    return res

a=[20,11,10,10070,7]
print(solution(a))