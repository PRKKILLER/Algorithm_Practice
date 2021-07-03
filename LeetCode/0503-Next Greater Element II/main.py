"""  
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. 
If it doesn't exist, return -1 for this number.


Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res, stk = [-1] * len(nums), []

        # loop once, we can get the next greater elem of normal array
        for i, num in enumerate(nums):
            while stk and nums[stk[-1]] < num:
                res[stk.pop()] = num

            stk.append(i)

        # loop twice, we can get the next graeter elem of circular array
        # since the second loop can deal with the condition:
        # arr[i] > arr[j], where i < j and there is no arr[k] > arr[j] where k > j
        for i, num in enumerate(nums):
            while stk and nums[stk[-1]] < num:
                res[stk.pop()] = num

            if not stk:
                break

        return res
