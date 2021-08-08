"""  
You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, 
where obstacles[i] describes the height of the ith obstacle.

For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course 
in obstacles such that:

- You choose any number of obstacles between 0 and i inclusive.
- You must include the ith obstacle in the course.
- You must put the chosen obstacles in the same order as they appear in obstacles.
- Every obstacle (except the first) is taller than or the same height as the obstacle 
immediately before it.

Return an array ans of length n, where ans[i] is the length of the longest obstacle course 
for index i as described above.


Example 1:

Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [1], [1] has length 1.
- i = 1: [1,2], [1,2] has length 2.
- i = 2: [1,2,3], [1,2,3] has length 3.
- i = 3: [1,2,3,2], [1,2,2] has length 3.
"""

"""  
This question can be viewed as an extension of the famous Longest Increasing Subsequence question.

The difference is that for this question, we need to consider duplicates and 
we need to get the longest non-descending sequence length for each index.

use tail array to track the current longest increasing subsequence. 
The difference is that when we meet duplicates, we will expand tails size, 
so I used binary search that search for upper bound.
"""


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        tails = [0] * n
        res = [1] * n
        size = 0

        for idx, num in enumerate(obstacles):
            lo, hi = 0, size
            while lo < hi:
                mid = (lo + hi) // 2
                if num < tails[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            tails[lo] = num
            size = max(lo + 1, size)
            res[idx] = lo + 1

        return res
