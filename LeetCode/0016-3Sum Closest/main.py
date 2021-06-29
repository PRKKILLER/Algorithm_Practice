"""  
Given an array nums of n integers and an integer target, find three integers in nums such that 
the sum is closest to target. Return the sum of the three integers. You may assume that each input would have 
exactly one solution.


Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""


class Solution:
    # two-pointers, similar to the 3sum solution
    # this question is actually simpler than 3 sum, since it doesn't require remove duplicates
    # overall time complexity: O(NlogN) + O(N^2) = O(N^2)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0] + nums[1] + nums[2]
        if res == target:
            return target

        min_diff = abs(target - res)
        nums.sort()

        for i in range(len(nums) - 2):
            t = target - nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                cur_sum = nums[lo] + nums[hi]
                if cur_sum == t:
                    return target

                cur_diff = abs(t - cur_sum)
                if cur_diff < min_diff:
                    min_diff = cur_diff
                    res = cur_sum + nums[i]

                if cur_sum < t:
                    lo += 1
                else:
                    hi -= 1

        return res
