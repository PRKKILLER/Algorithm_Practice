"""  
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.
"""

"""
思路： index as hash key
首先排除所有 <= 0 的元素，得到剩余长度 n
关键：the first missing positive is for sure smaller or equal to n + 1
对于长度为 n 的数组，第一个missing的positive number 一定 <= n
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cnt = 0 # count the positive element in the array
        
        # base case
        if 1 not in nums:
            return 1
        
        # [1]
        if len(nums) == 1:
            return 2
        
        for num in nums:
            if num > 0: cnt += 1
                
        mp = [0] * cnt
        
        for num in nums:
            if num <= cnt and num > 0:
                mp[num-1] = 1
                
        for i in range(cnt):
            if mp[i] == 0:
                return i + 1
            
        return cnt + 1