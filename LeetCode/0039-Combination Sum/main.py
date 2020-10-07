"""  
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations 
for the given input.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""

"""  
这题的难点在于可以重复使用同一个数字多次
对于backtrack算法，可以定义 next_start 来去重。又因为可以多次使用同一数字，
因此在使用完该数字之后，不用立刻改变 next_start 的值，可以give current number a second chance
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def backtrack(track, cur_sum, next_start):
            if cur_sum > target:
                return
            elif cur_sum == target:
                res.append(track[:])
                return
            
            for i in range(next_start, n):
                track.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(track, cur_sum+candidates[i], i)
                track.pop()
        
        backtrack([], 0, 0)
        return res