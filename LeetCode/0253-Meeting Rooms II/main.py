"""  
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

import heapq

"""  
思路，利用priority queue来track当前最早结束的会议
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or not intervals[0]:
            return 0

        if len(intervals) == 1:
            return 1

        # sort the meetings' start time in increasing order
        intervals.sort(key=lambda x: x[0])

        rooms = []

        # add the first meeting.
        # building the min heap
        heapq.heappush(rooms, intervals[0][1])

        for m in intervals[1:]:
            # if the currently earlist end time < meeting's start time
            # assign this meeting room to the new meeting
            if rooms[0] <= m[0]:
                heapq.heappushpop(rooms, m[1])
            else:
                heapq.heappush(rooms, m[1])

        return len(rooms)
