"""  
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

Example 1:

Input: [1,2,3]
Output: 6
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # elements in nums can be negative, so the largest product can be formed by 
        # one of the following 2 forms:
        # 1. nums[0] * nums[1] * nums[-1]
        # 2. nums[-1] * nums[-2] * nums[-3]
        
        return max(
            nums[0] * nums[1] * nums[-1],
            nums[-3] * nums[-2] * nums[-1]
        )

    def maximumProduct2(self, nums: List[int]) -> int:
    # the idea of this problem is simply find the 3 largest elements and 2 smallest elements in the array
    
        max1 = max2 = max3 = -1001
        min1 = min2 = 1001

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1*max2*max3, min1*min2*max1)