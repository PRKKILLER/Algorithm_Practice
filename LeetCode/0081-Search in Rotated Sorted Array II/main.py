"""  
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to "Search in Rotated Sorted Array", where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""

"""
这道题的难点在于可能存在duplicate，则可能出现 eg. [1,1,3,1], [3,1,1].这两种情况，中间值 = 最右侧值时
当 target = 3 时，可能出现在左半边数组或者右半边数组
对于该种情况，只需要将 hi 指针向左移动，缩小搜索的区间，进行下一次循环

worst case:
Example: [1,1,1,1,1] target=2
该情况下, 因为有duplicates的存在，因此每次只能一位 hi 指针，所以worst case 时间复杂度为 O(n)
Best Case: O(logN): without duplicate
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = (lo+hi)//2
            if nums[mi] == target:
                return True
            
            if nums[mi] < nums[hi]:
                if nums[mi] < target and target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
            elif nums[mi] > nums[hi]:
                if nums[mi] > target and nums[lo] <= target:
                    hi = mi - 1
                else:
                    lo = mi + 1
            elif nums[mi] == nums[hi]: # 向左移hi指针，缩小搜索范围
                hi -= 1
                
        return False