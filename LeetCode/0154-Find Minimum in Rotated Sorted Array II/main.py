"""  
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Input: [2,2,2,0,1]
Output: 0
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while nums[lo] >= nums[hi] and hi >= 0:
            if nums[lo] == nums[hi]:
                hi -= 1
                continue
            
            mid = (lo+hi)//2
            if nums[mid] < nums[hi]: # right part is sorted
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi -= 1
        
        return nums[lo]