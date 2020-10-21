"""  
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        for the start of the consecutive sequence, only when (start-1) not in nums
        then this element can has the possibility to become the start of the consecutive sequence
        
        the trick of this problem is to first store all the numbers in a HashSet to allow O(1) lookups
        
        Time complexity = O(N) + O(N) = O(N)
        """
        
        if len(nums) < 2: return len(nums)
        
        num_set = set(nums)
        
        max_len = 1
        
        for num in num_set:
            # important: only do the while loop when the element can be the start of consecutive sequence
            # so the while loop can only run for n iterations throughout the entire runtime of the algorithm
            if num - 1 not in num_set:
                cur_start = num
                cur_len = 1
                while cur_start + 1 in num_set:
                    cur_start += 1
                    cur_len += 1
                
                max_len = max(max_len, cur_len)
        
        return max_len
