"""  
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            tmp = [item + [num] for item in res]
            res += tmp
        
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """
        方法2： backtrack Power set is all possible combinations of all possible lengths, from 0 to n.
        1. get all subsets of length 0
        2. get all subsets of length 1
        ...
        n. get all subsets of length n
        """
        def backtrack(start, cur, sz):
            if len(cur) == sz:
                ret.append(cur[:])
                return
            
            for i in range(start, n):
                cur.append(nums[i]) # make choice
                backtrack(i + 1, cur, sz) # find all combination start with cur
                cur.pop()
        
        ret = []
        n = len(nums)
        # 每个循环得到不同长度的subsets
        for sz in range(n + 1):
            backtrack(0, [], sz)
            
        return ret