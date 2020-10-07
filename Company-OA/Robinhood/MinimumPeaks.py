"""  
Given an array of pairwise distinct positive integers arr=[1,9,7,8,2,6] populate the result array 
by returning minimum peaks.

Definition:

a[i-1] < a[i] > a[i+1]

Example:
Input: arr=[1,9,7,8,2,6]

First min peak = 6 [1,9,7,8,2]
Second min peak = 8 [1,9,7,2]
Third min peak = 9 [1,7,2]
Fourth min peak = 7 [1,2]
Fifth min peak = 2 [1]
Sixth min peak = 1

output: [6,8,9,7,2,1]
"""
from heapq import *

def solution(arr):
    arr = arr[:]  # make copy (optional)
    ans = []
    while True:
        # find the min peak
        best = None
        for i in range(len(arr)):
            if i > 0 and arr[i] <= arr[i-1]:
                continue
            if i+1 < len(arr) and arr[i] <= arr[i+1]:
                continue
            if best is None or arr[i] < arr[best]:
                best = i
        if best is None:
            # no more min peaks
            return ans
        else:
            # remove the min peak
            ans.append(arr.pop(best))

    return ans


# optimized approach

def min_peaks(arr):
    n = len(arr)

    # add sentinel
    arr.append(float('-inf'))
    ans = []

    # represents doubly-linked list
    # 0 <-> 1 <-> ... <-> n <-> 0
    prv = [n] + list(range(n))
    nxt = list(range(1, n+1)) + [0]

    # initialize min-heap of peaks
    peaks = []
    def _check_peak(i):
        if arr[prv[i]] < arr[i] > arr[nxt[i]]:
            heappush(peaks, (arr[i], i))

    for i in range(n):
        _check_peak(i)

    # remove min peak and check neighbors
    while peaks:
        val, i = heappop(peaks)
        ans.append(val)
        # before: j <-> i <-> k
        j, k = prv[i], nxt[i]
        prv[k] = j
        nxt[j] = k
        # after: j <-> k
        _check_peak(j)
        _check_peak(k)

    # remove sentinel (optional)
    # arr.pop()
    return ans

print(min_peaks([1,9,7,8,2,6]))