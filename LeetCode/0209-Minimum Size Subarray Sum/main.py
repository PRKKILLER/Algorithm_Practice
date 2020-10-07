"""  
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray 
of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""
from typing import List

class Solution:
    """ 
    1. O(n) solution: sliding window, 双指针法
    """
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        lo, hi, n = 0, 0, len(nums)
        min_s = n + 1 # min size of the sliding window
        win = 0 # sliding window

        while hi < n:
            win += nums[hi]
            hi += 1
            while win >= s:
                min_s = min(min_s, hi - lo)
                # 移动左指针
                win -= nums[lo]
                lo += 1
        
        return min_s if min_s < n + 1 else 0