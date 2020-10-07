"""  
For a given array a, find the maximum value of a[j]-a[i] for all i, j where:
a[i] <= a[j]
a[i] is odd, a[j] is even
If there are no lower indexed smaller items that are odd for all the even integers, then return -1
"""
from typing import List

def solution(arr: List[int]) -> int:
    if len(arr) < 2: return -1

    i, j = -1, -1
    for idx in range(len(arr)):
        if arr[idx] % 2: # odd number
            if i == -1 or arr[idx] < arr[i] and idx < j:
                i = idx
        if not arr[idx] % 2: # even number
            if i == -1:
                continue
            if arr[idx] > arr[j]:
                j = idx

    if i == -1 or j == -1:
        return -1

    return arr[j] - arr[i]

arr = [2,2,3,6,4]
print(solution(arr))
