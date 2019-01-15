class solution:
    '''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

    '''
    # solution-1: 两层循环，暴力求解
    def two_sum_s1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    # 思路：因为题目说明只有一个解，因此可以便利一遍数组，元素存放在dict中。并将数组下标作为value,数组值作为keys
    # 解题关键：运用哈希表
    def two_sum_s2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """      
        keys = {}
        for idx, value in enumerate(nums):
            check = target - value
            if check in keys: # 查询的是dict的keys
                return [keys[check], idx]
            keys[value] = idx