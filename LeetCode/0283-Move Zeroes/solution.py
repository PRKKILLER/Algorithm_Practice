class Solution():
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
    # 单指针

    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i, num in enumerate(nums):
            if num != 0:
                if pos != i:
                    # num[pos], num[i] = num[i], num[pos]
                    num[pos], num[i] = num[i], 0
                pos += 1

        return

    # shift non-zero numbers as far forward as possible,
    # fill remaining spaces with zeros
    def moveZeroes_v2(self, nums: List[int]) -> None:
        cur = 0
        for num in nums:
            if num != 0:
                nums[cur] = num
                cur += 1

        for i in range(cur, len(nums)):
            nums[i] = 0

        return
