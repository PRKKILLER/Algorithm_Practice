"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 3:

Input: [0,3,2,1]
Output: true
"""

"""
思路：双指针，分别从数组的两边出发，若数组中不存在重复值，且满足mountain array的定义，则两个指针会在同一个地方相遇。
并且要保证相遇的地点不在数组的第一个位置和最后一个位置
"""

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        
        i, j = 0, n - 1
        while i + 1 < n and A[i] < A[i+1]:
            i += 1
        while j > 0 and A[j] < A[j-1]:
            j -= 1
        
        return 0 < i == j < n - 1