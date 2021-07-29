"""  
Given an array nums of n integers where n > 1,  return an array output such that output[i] 
is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any 
prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
"""


class Solution:
    """  
    Key insights: keep tracking of left and right product lists
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_prod, right_prod = [1] * n, [1] * n
        res = [0] * n

        # left_prod[i] is the product of all elements to the left
        for i in range(1, n):
            left_prod[i] = left_prod[i-1] * nums[i-1]

        # right_prod[i] is the product of all elements to the right
        for i in range(n-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]

        for i in range(n):
            res[i] = left_prod[i] * right_prod[i]

        return res

    """  
    O(1) space solution
    keep tracking of the right_product results on the fly
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        # 1. initailize res array as left_product list
        # where res[i] is the product of numbers on the left
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]

        # keep tracking the right_product results regarding index i
        r_product = 1

        # update the res array and "r_product" on the fly
        for i in range(n - 1, -1, -1):
            res[i] *= r_product
            r_product *= nums[i]

        return res
