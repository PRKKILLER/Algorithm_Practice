"""  
You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n 
binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the root that is guaranteed to be empty, 
and you do not have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). 
The robot with the four given APIs can move forward, turn left, or turn right. 
Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, 
and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Note that the initial direction of the robot will be facing up. 
You can assume all four edges of the grid are all surrounded by a wall.


Custom testing:

The input is only given to initialize the room and the robot's position internally. 
You must solve this problem "blindfolded". In other words, you must control the robot using only 
the four mentioned APIs without knowing the room layout and the initial robot's position.
"""

# This is the robot's control interface.


class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        pass

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        pass


class Solution:
    """  
    Intuition

This solution is based on the same idea as maze solving algorithm called "right-hand rule". 
Go forward, cleaning and marking all the cells on the way as visited. 
At the obstacle turn right, again go forward, etc. Always turn right at the obstacles and 
then go forward. Consider already visited cells as virtual obstacles.

What do do if after the right turn there is an obstacle just in front ?

Turn right again.

How to explore the alternative paths from the cell ?

Go back to that cell and then turn right from your last explored direction.

When to stop ?
Stop when you explored all possible paths, 
i.e. all 4 directions (up, right, down, and left) for each visited cell.
    """

    def cleanRoom(self, robot: Robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(pos, dx, dy):
            visited.add(pos)
            robot.clean()

            # going clockwise (up, right, down, left)
            for i in range(4):
                new_pos = (pos[0] + dx, pos[1] + dy)
                if new_pos not in visited and robot.move():
                    backtrack(new_pos, dx, dy)
                    go_back()

                # turn the robot clockwise
                robot.turnRight()
                # turn right
                dx, dy = dy, -dx

        visited = set()
        backtrack((0, 0), -1, 0)
