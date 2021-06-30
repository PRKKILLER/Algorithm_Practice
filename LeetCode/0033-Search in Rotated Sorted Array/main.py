"""  

"""


"""
该题有下列两种情况：
对于1个有序数组[1,2,3,4,5,6,7,8]

情况1：[4,5,6,7,8,1,2,3]
数组的 mid = 3, arr[mid] = 7 arr[mid] > arr[-1], 则说明mid左侧的元素是有序的，mid右侧的部分
重新组成了一个rotated sorted array。此时判断target和arr[mid]的大小，即可缩小搜索范围

情况2：[6,7,8,1,2,3,4,5]
数组的 mid = 3, arr[mid] = 1, arr[mid] < arr[-1], 则说明mid右侧的元素是有序的，mid左侧的部分是无序的
mid左侧的部分重新组成了roated sorted array。
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[hi]:  # right side array is sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:  # left side array is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

        return -1
