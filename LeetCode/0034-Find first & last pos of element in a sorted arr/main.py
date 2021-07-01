"""  
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

"""


class Solution:
    # binary search with <=
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def searchLow():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo+hi)//2
                if target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            return lo

        def searchHigh():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo+hi)//2
                if target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            return lo - 1

        min_rank = searchLow()
        max_rank = searchHigh()
        if 0 <= min_rank < len(nums) and min_rank <= max_rank and nums[min_rank] == target:
            return [min_rank, max_rank]

        return [-1, -1]

        ################################################################

    # binary search with <
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # find the lowest rank of the given target
        min_rank = self.binSearchFirst(nums, target)
        if min_rank == -1:
            return [-1, -1]

        # find the highest rank of the given target
        max_rank = self.binSearchLast(nums, target)

        return [min_rank, max_rank]

    def binSearchFirst(self, arr, target):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi)//2
            if target <= arr[mid]:
                hi = mid
            else:
                lo = mid + 1

        if lo == len(arr) or arr[lo] != target:
            return -1

        return lo

    def binSearchLast(self, arr, target):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi)//2
            if target < arr[mid]:
                hi = mid
            else:
                lo = mid + 1

        return lo - 1 if arr[lo-1] == target else -1
