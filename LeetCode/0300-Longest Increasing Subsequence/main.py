"""  
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.


Follow up: Could you improve it to O(n log n) time complexity?
"""

from typing import List

class Solution:
    """  
    注意不是substring，是subsequence, 因此数字不用相邻
    思路：利用动态规划, dp[i]保存以i结尾的最长递增子串
    对于每个nums[i]，从0遍历到i，当遇到比nums[i]的数字的时候，更新dp[i]
    dp[i] = max(dp[i], dp[j]+1)

    时间复杂度： O(n^2)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    """  
    该题可以用二分查找的方法提速，使得时间复杂度=O(nlong)
    首先建立一个空的dp数组，然后开始遍历原数组，对于每个遍历到的数字，我们用二分查找在dp数组中查找
    第一个不小于它的数字。若不存在，则说明当前数字是最大的，则直接append到dp数字的最后
    若存在，则找到dp数组的原数字，用新的数字更新原数字
    """
    def lengthOfLIS2(self, nums):
        if len(nums) < 2: return len(nums)

        dp = []

        for num in nums:
            idx = self.lowerBound(dp, 0, len(dp), num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num

        return len(dp)

    def lowerBound(self, arr, lo, hi, target):
        while lo < hi:
            mi = (lo + hi) // 2
            if target <= arr[mi]:
                hi = mi
            else:
                lo = mi + 1

        return lo

arr = [10,9,2,5,3,7,101,18]
sol = Solution()
res = sol.lengthOfLIS2(arr)
print(res)