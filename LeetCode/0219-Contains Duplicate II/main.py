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
        cache = set()
        for i in range(len(nums)):
            if nums[i] in cache:
                return True
            cache.add(nums[i])
            if len(cache) > k:
                cache.remove(nums[i-k]) # remove the oldest element from set
                
        return False