"""  
Find the minimum number of groups who's sum of each group is at max 3, and every element must be in a group.
Given an Array like: [1.01, 1.01, 3.0, 2.7, 1.99, 2.3, 1.7]
return the minimum number of groups, in this case it would be 5 groups: (1.01 , 1.99), (1.01, 1.7), (3.0), (2.7), (2.3)

Constraint: all elements are between 1.01-3 inclusive, and each groups sum is at max 3
"""

def solution(arr):
    arr = sorted(arr)
    cnt = 0
    lo, hi = 0, len(arr) - 1
    
    while lo <= hi:
        if lo == hi:
            cnt += 1
            break
        if arr[lo] + arr[hi] <= 3:
            lo += 1
            hi -= 1
            cnt += 1
        else:
            hi -= 1
            cnt += 1

    return cnt