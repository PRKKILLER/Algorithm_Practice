"""  
Given an integer array nums, return the number of triplets chosen from the array that can make triangles 
if we take them as side lengths of a triangle.

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
"""


class Solution:
    """  
    similar question: 3sum smaller
    the trick part of this problem is to traverse from right to left
    otherwise, we will miss some cases, and don't know how to move the left and right pointers
    """

    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        sz, res = len(nums), 0

        for k in range(sz - 1, 1, -1):
            lo, hi = 0, k - 1
            while lo < hi:
                if nums[lo] + nums[hi] > nums[k]:
                    # every number between [lo, hi] satisfy the condition that a + b > c
                    res += hi - lo
                    hi -= 1
                else:
                    lo += 1

        return res
