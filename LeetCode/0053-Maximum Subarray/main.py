"""  
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution 
using the divide and conquer approach, which is more subtle.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


"""  
Greedy search

用 res 保存全局连续最大值，cur_sum 保存局部连续最大值
从左向右遍历，比较 cur_sum + num 和 num 的大小，若cur_sum + num < num，则舍弃之前的 cur_sum
使得 cur_sum = num
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, cur_sum = float('-inf'), 0
        
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            res = max(res, cur_sum)
            
        return res

    # 动态规划
    def maxSubArray2(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + nums[i-1], nums[i])
            res = max(res, nums[i])
        
        return res