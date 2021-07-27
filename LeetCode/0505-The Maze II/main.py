"""  
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). 
The ball can go through the empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. 
When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, 
where start = [startrow, startcol] and destination = [destinationrow, destinationcol], 
return the shortest distance for the ball to stop at the destination. 
If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) 
to the destination (included).

You may assume that the borders of the maze are all walls (see examples).

Example:

Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], 
start = [0,4], destination = [4,4]

Output: 12
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Reference:

https://leetcode.com/problems/the-maze-ii/discuss/98427/2-Solutions%3A-BFS-and-Dijkstra's.-Detailed-explanation..-But-why-is-BFS-faster
"""


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
        Dijkstra algorithm using Priority Queue

        Dijkstra's Algo seems to be an optimization of the first solution, since
        1. we always select the node with the least cost
        2. do not revisit visited nodes
        3. terminate straight away when we find the destination.
        """
        import heapq
        m, n = len(maze), len(maze[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # down, left, up, right
        pq = [(0, start[0], start[1])]  # (step, x, y)
        stoppable = {(start[0], start[1]): 0}

        while pq:
            # popping out the least distance from pq (Dijkstra)
            step, x, y = heapq.heappop(pq)
            if [x, y] == destination:
                return step

            for dx, dy in dirs:
                row, col = x + dx, y + dy
                move = step + 1
                while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:
                    row += dx
                    col += dy
                    move += 1
                row -= dx
                col -= dy
                move -= 1
                if (row, col) not in stoppable or move < stoppable[(row, col)]:
                    stoppable[(row, col)] = move
                    heapq.heappush(pq, (move, row, col))

        return -1
