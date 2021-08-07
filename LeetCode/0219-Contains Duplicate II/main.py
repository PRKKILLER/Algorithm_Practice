"""  
Given an array of integers and an integer k, find out whether there are two distinct 
indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j 
is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        dic = {}
        for idx, num in enumerate(nums):
            if num in dic:
                if idx - dic[num] <= k:
                    return True
                else:
                    dic[num] = idx
            else:
                dic[num] = idx

        return False
