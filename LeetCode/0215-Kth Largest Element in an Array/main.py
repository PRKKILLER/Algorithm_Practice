""" 
Find the kth largest element in an unsorted array. Note that it is the kth 
largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
"""

class Solution:
    def findKthLargest(self, nums, k):
        # 将 k 改写为正数第 k 大的数字
        k = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            pivot = self.partition(nums, lo, hi)
            if pivot < k:
                lo = pivot + 1
            elif pivot > k:
                hi = pivot - 1
            else:
                break
        return nums[k]

    def partition(self, arr, lo, hi):
        tmp = arr[lo]
        while lo < hi:
            while lo < hi and tmp <= arr[hi]: hi -= 1
            if lo < hi:
                arr[lo] = arr[hi]
                lo += 1
            while lo < hi and arr[lo] <= tmp: lo += 1
            if lo < hi:
                arr[hi] = arr[lo]
                hi -= 1
        arr[lo] = tmp
        return lo

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]