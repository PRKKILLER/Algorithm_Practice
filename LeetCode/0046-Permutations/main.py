"""  
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        
        res, n = [], len(nums)
        
        def backtrack(track):
            if len(track) > n: return
            elif len(track) == n:
                res.append(track[:])
                
            for num in nums:
                if num not in track:
                    track.append(num)
                    backtrack(track)
                    track.pop()
                    
        backtrack([])
        return res