"""  
Given an integer array nums, find a contiguous non-empty subarray within the array 
that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""


class Solution:
    """  
    Idea: Kadane's algorithm
    """

    def maxProduct(self, nums: List[int]) -> int:
        # max_product: maximum product up to that number
        # min_product: minimum product up to that number
        res = max_product = min_product = nums[0]

        for i in range(1, len(nums)):
            tmp_max = max(nums[i], nums[i] * max_product,
                          nums[i] * min_product)
            min_product = min(nums[i], nums[i] *
                              max_product, nums[i] * min_product)
            max_product = tmp_max

            res = max(res, max_product)

        return res

    def maxProduct(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/maximum-product-subarray/discuss/48302/2-Passes-scan-beats-99

        This is really about odd or even negative numbers.
        if it's odd, either the left end one or the right end one should be counted, 
        so it will be revealed by scanning from left and from right in 2 passes.

        0 is like a delimiter, product accumulation will be reset to 1
        """
        n = len(nums)
        res = float('-inf')
        product = 1

        # left to right traverse
        for d in nums:
            product *= d
            res = max(res, product)
            if d == 0:
                product = 1

        # right to left traverse
        product = 1
        for d in nums[::-1]:
            product *= d
            res = max(res, product)
            if d == 0:
                product = 1

        return res
