class Solution(object):
    '''
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
    '''

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        from collections import defaultdict
        dd = defaultdict(lambda : 0)
        for item in nums:
            dd[item] += 1
        return max(sorted(zip(dd.values(), dd.keys())))[1] # 利用zip交换key, value的顺序，进行排序

    def majorityElement_v2(self, nums):
        """
            :type nums: List[int]
            :rtype: int
        """
        match = set(nums)
        for item in match:
            if nums.count(item) > (len(nums) / 2):
                return item

    def majorityElement_v3(self, nums):
        """
            :type nums: List[int]
            :rtype: int
        """
        from collections import Counter
        d = Counter(nums)
        return max(d, key=d.get)

print(Solution().majorityElement_v3([1,1,1,3,3,2]))