"""  
Given a collection of intervals, find the minimum number of intervals you need to remove to make the 
rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        the problem is the same as "Given a collection of intervals, 
        find the maximum number of intervals that are non-overlapping."
        
        题目要求移除最少的internval以达到non-overlapping,实际上是等同于寻找最多的non-overlapping
        interval。是典型的贪心算法的问题
        """
        if len(intervals) == 0: return 0
        
        intervals = sorted(intervals, key=lambda x: x[1])
        cnt, end = 1, intervals[0][1]
        
        for pair in intervals[1:]:
            if pair[0] >= end:
                cnt += 1
                end = pair[1]
                
        return len(intervals) - cnt