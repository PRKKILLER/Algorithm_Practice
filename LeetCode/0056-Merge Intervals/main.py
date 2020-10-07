"""  
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

注意：intervals数组并不是有序的，因此需要先排序

Constraints:

intervals[i][0] <= intervals[i][1]
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []
        
        intervals = sorted(intervals, key=lambda x: x[0]) # 找到最小的start
        
        start, end = intervals[0][0], intervals[0][1]
        res = []
        
        for pair in intervals[1:]:
            if pair[0] <= end:        # 存在overlapping
                end = max(pair[1], end)  # 更新上界
            else:
                res.append([start, end])
                start, end = pair[0], pair[1]
        
        res.append([start, end])
        return res
