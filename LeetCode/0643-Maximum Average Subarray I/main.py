"""  
Given an array consisting of n integers, find the contiguous subarray of given length k that has the 
maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = win = sum(nums[:k])
        
        for i in range(1, len(nums)-k+1):
            win = win - nums[i-1] + nums[i+k-1]
            res = max(res, win)
            
        return res / k