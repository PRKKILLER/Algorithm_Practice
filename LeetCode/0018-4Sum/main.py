"""  
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""

from typing import List


class Solution:
    # based on the 3sum solution
    # time complexity: O(N^3)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        if nums[0] * 4 > target:
            return []

        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] * 4 > target:
                break

            three_sum_res = self._threeSum(nums[i+1:], target - nums[i])
            res += [[nums[i]] + arr for arr in three_sum_res]

        return res

    def _threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] * 3 > target:
                break

            t = target - nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] == t:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1

                elif nums[lo] + nums[hi] < t:
                    lo += 1
                else:
                    hi -= 1

        return res
