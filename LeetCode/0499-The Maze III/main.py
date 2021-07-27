"""  
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). 
The ball can go through the empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. 
There is also a hole in this maze. The ball will drop into the hole if it rolls onto the hole.

Given the m x n maze, the ball's position ball and the hole's position hole, 
where ball = [ballrow, ballcol] and hole = [holerow, holecol], 
return a string instructions of all the instructions that the ball should follow to drop in the hole 
with the shortest distance possible. If there are multiple valid instructions, 
return the lexicographically minimum one. If the ball can't drop in the hole, return "impossible".

If there is a way for the ball to drop in the hole, 
the answer instructions should contain the characters 
'u' (i.e., up), 'd' (i.e., down), 'l' (i.e., left), and 'r' (i.e., right).

The distance is the number of empty spaces traveled by the ball from the start position 
(excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).

Example 1:
Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [0,1]
Output: "lul"
Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller 
because 'l' < 'u'. So the output is "lul".
"""


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        """
        Similar to Maze-2 puzzle, we can still use Dijkstra Algo to find the shortest path
        to the stoppable points

        The difference here is that ball can stop when reach the wall or reach the hole,
        so we should break the while loop when hole is encountered
        """
        import heapq
        m, n = len(maze), len(maze[0])
        dirs = [(1, 0, 'd'), (0, -1, 'l'), (-1, 0, 'u'),
                (0, 1, 'r')]  # down, left, up, right
        pq = [(0, '', ball[0], ball[1])]  # (step, pattern, x, y)
        stoppable = {tuple(ball): (0, '')}

        while pq:
            step, pattern, x, y = heapq.heappop(pq)
            if [x, y] == hole:
                return pattern

            for dx, dy, p in dirs:
                row, col = x, y
                move = step
                while 0 <= row + dx < m and 0 <= col + dy < n and maze[row+dx][col+dy] != 1:
                    row += dx
                    col += dy
                    move += 1
                    if [row, col] == hole:
                        break

                if (row, col) not in stoppable or (move, pattern + p) < stoppable[(row, col)]:
                    stoppable[(row, col)] = (move, pattern + p)
                    heapq.heappush(pq, (move, pattern + p, row, col))

        return 'impossible'
