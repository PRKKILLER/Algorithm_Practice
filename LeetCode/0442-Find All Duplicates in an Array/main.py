"""  
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

class Solution:
    # 因为1 ≤ a[i] ≤ n，因此可以想到利用a[i]做索引，但是关键在于怎样记录已经访问过的位置
    # 思路：当第一次访问nums[nums[i]]时，将nums[nums[i]] = -nums[nums[i]]
    # 若再次访问到同一数字时，就会遇到负数，则即为重复数字
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx-1] > 0:
                nums[idx-1] *= -1
            else:
                res.append(idx)
            
        return res