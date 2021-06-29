"""  
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

# time complexity: O(N^2)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # sanity check
        if not nums or nums[0] > 0 or nums[-1] < 0:
            return []

        res = []
        for idx in range(len(nums)-2):
            if nums[idx] > 0:
                break

            # skip duplicates
            if idx > 0 and nums[idx-1] == nums[idx]:
                continue

            target = -nums[idx]
            lo, hi = idx + 1, len(nums) - 1
            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    res.append([nums[idx], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # skip duplicates
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1

                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    hi -= 1

        return res
