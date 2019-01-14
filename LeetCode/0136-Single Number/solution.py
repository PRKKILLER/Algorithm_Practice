class Solution:
    '''
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
    '''
    
    # 对数组先进行排序, 该方法空间复杂度为o(0)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() # sort the list in-place
        for i in range(1, len(nums), 2): # 若 i + step > len(nums)-1, 则直接跳出循环
            if nums[i] != nums[i - 1]:
                return nums[i -1]
        return nums[-1]

    # 采用XOR运算
    def singleNumber_v2(self, nums):
        """
            :type nums: List[int]
            :rtype: int
        """
        match = 0
        for item in nums:
            match = match ^ item
        return match


    def singleNUmber_v3(self, nums):
        """
            :type nums: List[int]
            :rtype: int
        """
        from collections import Counter
        return Counter(nums).most_common()[-1][0]

test = Solution().singleNumber([1,1,3])