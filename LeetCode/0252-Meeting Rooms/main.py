"""  
Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.


Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True

        intervals = sorted(intervals, key=lambda x: x[0])
        end = intervals[0][1]

        for inter in intervals[1:]:
            if end > inter[0]:
                return False
            end = inter[1]

        return True
