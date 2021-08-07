"""  
You are given an m x n matrix M initialized with all 0's and an array of operations ops, 
where ops[i] = [ai, bi] means M[x][y] should be incremented by one 
for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
"""

"""  
Observation: since every area in the ops list is start from origin, end at position ops[i]
If we want to count the area with biggest values, we need to find the area with most overlapping.
"""


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        min_height = min(op[0] for op in ops)
        min_width = min(op[1] for op in ops)

        return min_height * min_width
