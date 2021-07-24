"""  
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.


Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

1. 0 <= intervals.length <= 104
2. intervals[i].length == 2
3. 0 <= intervals[i][0] <= intervals[i][1] <= 105
4. intervals is sorted by intervals[i][0] in ascending order.
5. newInterval.length == 2
6. 0 <= newInterval[0] <= newInterval[1] <= 105
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx, n = 0, len(intervals)
        res = []

        # add all intervals ending before newInterval
        while idx < n and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1

        # merge all overlapping intervals into one big newInterval
        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1
        res.append(newInterval)

        # add all intervals beyound newInterval
        res.extend(intervals[idx:])

        return res
