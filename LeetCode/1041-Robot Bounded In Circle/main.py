"""  
On an infinite plane, a robot initially stands at (0, 0) and faces north. 
The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """  
        1. if robot returns to (0,0), its trajectory will be circle
        2. if robot finishes the instructions without facing toward north,
        then robot will return to origin in another 3 or 1 round
        """
        x, y, dx, dy = 0, 0, 0, 1

        for ins in instructions:
            if ins == 'G':
                x, y = x + dx, y + dy
            elif ins == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
