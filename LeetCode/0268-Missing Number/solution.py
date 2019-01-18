class Solution(object):
    '''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:

    Input: [3,0,1]
    Output: 2

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
    '''

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import numpy as np
        lookup = np.zeros(len(nums) + 1)

        for item in nums:
            lookup[item] = 1
        return int(lookup.argmin())

    # O(1) space complicity
    def missingNumber_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) + 1):
            if i in nums: continue
            else: return i

    # 等差数列前n项和减去数组之和(注意是从0开始）n = len(nums)
    def missingNumber_v3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        return length * (length + 1) // 2 - sum(nums)

    # 异或位运算
    # 因为两次相同数(异或运算^)互相抵消，ex：res ^ 1 ^ 1 = res ^ (1 ^ 1) = res ^ 0 = res
    # 0 ~ n总共(n+1)个数,res进行2n次运算后，最后得到的结果就是missing number
    def missingNumber_v4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = n = len(nums)
        for i in range(n):
            res ^= i
            res ^= nums[i]
        return res


print(type(Solution().missingNumber_v3([3,0,1])))