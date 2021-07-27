"""  
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). 
The ball can go through the empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, 
where start = [startrow, startcol] and destination = [destinationrow, destinationcol], 
return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

Example:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], 
start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. 
Notice that you can pass through the destination but you cannot stop there.
"""


class Solution:
    """  
    该题解题的关键在于**只寻找球能够停下来的位置**，并且判断 destination 是否属于其中

    BFS solution
    Generally， we mark a point as visited when we first enque this point, instead of popping it out
    """

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        from collections import deque

        m, n = len(maze), len(maze[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # down, left, up, right
        dq = deque([start])
        maze[start[0]][start[1]] = 2  # mark as visited

        while dq:
            x, y = dq.popleft()
            if [x, y] == destination:
                return True

            for dx, dy in dirs:
                row, col = x + dx, y + dy
                # keep moving on the same direction until it hits the wall
                # only add "can stop" position to the queue
                while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:
                    row += dx
                    col += dy
                row -= dx
                col -= dy

                if maze[row][col] == 0:
                    dq.append([row, col])
                    # mark position as visited when enque
                    maze[row][col] = 2

        return False

    """  
    DFS solution
    """

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # down, left, up, right
        maze[start[0]][start[1]] = 2  # mark as visited

        def dfs(x: int, y: int) -> bool:
            if [x, y] == destination:
                return True

            # search stoppable position
            for dx, dy in dirs:
                row, col = x + dx, y + dy
                while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:
                    row += dx
                    col += dy
                row -= dx
                col -= dy
                if maze[row][col] == 0:
                    maze[row][col] = 2  # mark as visited
                    if dfs(row, col):
                        return True

            return False

        return dfs(start[0], start[1])
