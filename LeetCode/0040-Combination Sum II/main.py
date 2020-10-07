"""  
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def backtrack(track, cur_sum, next_start):
            if cur_sum > target:
                return
            elif cur_sum == target:
                tmp = sorted(track)
                if tmp not in res:
                    res.append(tmp)
                return
            
            for i in range(next_start, n):
                track.append(candidates[i])
                backtrack(track, cur_sum+candidates[i], i+1)
                track.pop()
                
        backtrack([], 0, 0)
        return res