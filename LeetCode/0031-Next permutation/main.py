"""  
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order 
(i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.


Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1. From right to left, find the first non ascending element
        pivot = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i - 1
                break

        # 2. if pivot=-1, which means the array now is the last permutation
        # return the reverse order of the current array, which is the lowest possible order
        if pivot == -1:
            nums.reverse()
            return

        # 3. if pivot != -1, start from the rightmost elment, find the first number
        # which is greater than the pivot, swap these two element
        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break

        # 4. now the element to the right side of the pivot becomes descending order
        # reverse the element to the right of the pivot
        s, e = pivot + 1, len(nums) - 1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

        return
