"""  
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b (注意该条件)

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
"""


class Solution:
    # time complexity: O(logN) + O(K)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        if x <= arr[0]:
            return arr[:k]

        if x >= arr[-1]:
            return arr[-k:]

        from collections import deque
        l = len(arr)
        lo, hi = 0, l - 1

        # binary search for the lowest rank of x;
        # if x doesn't exist, find the insert position for x
        while lo <= hi:
            mid = (lo+hi)//2
            if x <= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        if arr[lo] > x:
            if x - arr[lo-1] <= arr[lo] - x:
                lo -= 1

        res, k = deque([arr[lo]]), k - 1
        p1, p2 = lo - 1, lo + 1

        while k > 0:
            if p1 >= 0 and p2 < l:
                if x - arr[p1] <= arr[p2] - x:
                    res.appendleft(arr[p1])
                    p1 -= 1
                else:
                    res.append(arr[p2])
                    p2 += 1

            elif p1 < 0:
                res.append(arr[p2])
                p2 += 1
            elif p2 >= l:
                res.appendleft(arr[p1])
                p1 -= 1

            k -= 1

        return list(res)

    # Binary Search To Find The Left Bound
    """  
    If there needs to be k elements, then the left bound's upper limit is arr.length - k, 
    because if it were any further to the right, you would run out of elements to include in the final answer.

    consider two indices at each binary search operation, the usual "mid", and some index "mid + k". 
    The relationship between these indices is significant because only one of them could possibly be in a final answer. 
    For example, if mid = 2, and k = 3, then arr[2] and arr[5] could not possibly both be in the answer, 
    since that would require taking 4 elements [arr[2], arr[3], arr[4], arr[5]].

    If the element at arr[mid] is closer to x than arr[mid + k], then that means arr[mid + k], as well as every element to 
    the right of it can never be in the answer. This means we should move our right pointer to avoid considering them. 
    The logic is the same vice-versa - if arr[mid + k] is closer to x, then move the left pointer.
    """

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k

        while lo < hi:
            mid = (lo+hi)//2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid

        return arr[lo:lo + k]
