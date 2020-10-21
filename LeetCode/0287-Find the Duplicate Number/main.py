"""  
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] 
inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

- How can we prove that at least one duplicate number must exist in nums? 
- Can you solve the problem without modifying the array nums?
- Can you solve the problem using only constant, O(1) extra space?
- Can you solve the problem with runtime complexity less than O(n2)?

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow