"""  
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
"""

"""
对于rotated sorted array, 存在一个pivot，在该点位置处，递增的趋势会逆转
我们就需要找到这个位置

对于shifted part of the array，一直不变的性质就是 nums[lo] > nums[hi]
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        
        # the invariant property of a rotated sorted array is
        # nums[lo] > nums[hi]
        while nums[lo] > nums[hi]:
            mid = (lo+hi)//2
            if nums[mid] < nums[hi]: # right part of the array is sorted
                hi = mid
            else:
                lo = mid + 1
                
        return nums[lo]