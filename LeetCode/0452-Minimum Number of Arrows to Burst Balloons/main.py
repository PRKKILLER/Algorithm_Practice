"""  
There are a number of spherical balloons spread in two-dimensional space. For each balloon, 
provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, 
y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. 
Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. 
A balloon with x_start and x_end bursts by an arrow shot at x if x_start ≤ x ≤ x_end. 
There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up 
infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) 
and another arrow at x = 11 (bursting the other two balloons).
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """  
        本题的真实题意，就是找到最多的overlapping interval，非常像leetcode-56题，都是一个套路
        """
        if len(points) == 0: return 0
        
        points = sorted(points, key=lambda x: x[0])
        
        start, end = points[0][0], points[0][1]
        cnt = 1
        for pair in points[1:]:
            if pair[0] <= end:
                end = min(pair[1], end)
            else:
                cnt += 1
                start, end = pair[0], pair[1]
                
        return cnt