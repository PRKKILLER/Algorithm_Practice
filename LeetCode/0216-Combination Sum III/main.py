"""  
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order.


Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(track, cur_sum, next_start):
            if cur_sum > n: return
            if len(track) > k: return
            if len(track) == k:
                if cur_sum == n:
                    # make a copy of valid track
                    res.append(track[:])
                return
            
            # 每次从chosen digit的下一个数字开始循环
            # 也即next_start，这样就能保证了没有重复
            for i in range(next_start, 10):
                track.append(i)
                backtrack(track, cur_sum+i, i+1)
                track.pop()
                
        backtrack([], 0, 1)
        return res