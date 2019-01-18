class Solution(object):
    '''
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
    '''
    # 法1, 没有做到in-place
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
            nums.append(0)

    # 法2，双指针
    def moveZeroes_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0, p1 = 0, 0 # 双指针，p0指向0，p1指向非0元素
        length = len(nums)
        while p0 < length and p1 < length:
            if nums[p0] != 0:
                p0 += 1
                p1 = p0
                continue
            if nums[p1] == 0:
                p1 += 1
                continue
            # nums[p0] == 0 and nums[p1] != 0
            nums[p0], nums[p1] = nums[p1], nums[p0]
            p0 += 1
            p1 += 1

    # 单指针
    def moveZeroes_v3(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1

if __name__ == "__main__":
    a = [0,1,0,3,12]
    print(a.count(0))
    Solution().moveZeroes_v3(a)
    print(a)