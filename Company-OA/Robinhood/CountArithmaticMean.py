"""  
Given an array of integers a. Calculate how many numbers in the array are equal to the arithmetic mean of their
immediate neighbors.

In other words, count the number of indices i such that a[i-1]+a[i+1]=2*a[i]
Note: if a[u-1] or a[i+1] don't exist, they should be considered as 0
"""

def solution(arr):
    if not arr: return 0

    arr = [0] + arr + [0]
    cnt = 0
    for i in range(1, len(arr) - 1):
        if arr[i] * 2 == arr[i-1]+arr[i+1]:
            cnt += 1
    return cnt

a = [2,4,6,6,3]
print(solution(a))