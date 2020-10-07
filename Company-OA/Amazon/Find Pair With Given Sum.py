"""  
Given a list of positive integers nums and an int target, return indices of the two numbers such that 
they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have multiple pairs, select the pair with the largest number.

Example:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.
"""
from typing import List

def solution(nums: List[int], target: int) -> List[int]:
    target -= 30
    m = {}
    out = []

    for idx, num in enumerate(nums):
        if target - num in m:
            if not out or max(num, target - num) > max(nums[out[0]], nums[out[1]]):
                out = [m[target - num], idx]
        else:
            m[num] = idx

    return out

nums = [20, 50, 40, 25, 30, 10]
target = 90
print(solution(nums, target))