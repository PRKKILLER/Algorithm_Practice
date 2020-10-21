"""  
Given an array of n integers nums and an integer target, find the number of index triplets 
i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?


Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Constraints:

n == nums.length
0 <= n <= 300
-100 <= nums[i] <= 100
-100 <= target <= 100
"""

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        if n < 3:
            return 0
        
        res = 0
        for k in range(n - 2):
            tmp = target - nums[k]
            lo, hi = k + 1, n - 1
            while lo < hi:
                if nums[lo] + nums[hi] < tmp:
                    res += hi - lo
                    lo += 1
                else:
                    hi -= 1
                    
        return res