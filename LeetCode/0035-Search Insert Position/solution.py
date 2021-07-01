'''
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''


class Solution:
    # 采用binary search 的思想，运用二分法进行搜索
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, target)

    def binarySearch(self, nums, target):
        """
            Time:  O(log(n))
            Space: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # 向下取整
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def binSearchFirst(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo
