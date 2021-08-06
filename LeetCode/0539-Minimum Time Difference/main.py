"""  
Given a list of 24-hour clock time points in "HH:MM" format, 
return the minimum minutes difference between any two time-points in the list.

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:

2 <= timePoints <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""

"""  
The tricky part of this problem is to deal with the situation like "23:59" and "00:00"
Since time is like a circle 00:00 = 24:00, so the last one could be closest one to the first one
"""




from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time: str):
            h, m = map(int, time.split(':'))
            return h * 60 + m

        sorted_timestamps = sorted(map(convert, timePoints))
        # deal with the case when the last element actually is the cloest one to the first one
        sorted_timestamps.append(sorted_timestamps[0] + 60 * 24)
        return min(b - a for a, b in zip(sorted_timestamps, sorted_timestamps[1:]))
