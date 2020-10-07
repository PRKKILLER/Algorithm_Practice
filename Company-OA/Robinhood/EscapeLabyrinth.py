"""  
In a rectangular matrix, containing obstacles and teleports. Starting from the upper-left corner, you are
wondering if it's possible to reach the lower-right corner by only moving to the right.

n, m represents the dimensions of the labyrinth, as well as obstacles and teleports, which are lists containing
the coordinates of all the obstables and teleport respectively

Rules:
1. An obstables cannot be traversed: you must stop immediately if reach a cell containing an obstacle
2. A teleport is a pair of cells (start, end), where start is the starting cell of teleportation, and 
end is the destination cell. If you reach the start cell, you are immediately teleported to the end cell

Note: 
(1) it doesn't work backwards, you cannot teleport form end to start
(2) it is guaranteed that there are no teleport with same starting points
(3) start and end point cell of the teleport do not contain obstacles

Start on the cell with coord (0,0), goal is locate at the cell with coord (n-1,m-1)

Move according to the following rules:
1. Always move the right: if you are currently standing on the cell with coord(r, c), you will try to get to (r, c+1)
2. If the destination cell is the starting point of a teleport, proceed to the teleportation end point
3. If the destination cell either contains an obstacles or is outside the labyrinth bounds, stop moving and stay where
you are.

Find out whether you can reach the exit of the labyrinth by following the algorithm above. Return true if you will 
eventually reach the goal, and false otherwise

It is guaranteed that (0,0) and (n-1,m-1) do not contain an obstacle or the start point of a teleport

For example:
n=3,m=3, obstacles=[[2,1]], teleports=[[0,1,2,0]]
Output: false
"""

def solution(n, m, obstables, teleports):
    matrix = [[0] * m for _ in range(n)]
    for x, y in obstables:
        matrix[x][y] = '*'

    for s_x, s_y, e_x, e_y in teleports:
        matrix[s_x][s_y] = (e_x,e_y)

    r, c = 0, 0
    while r < n and c < m:
        if r == n-1 and c == m-1:
            return True

        if matrix[r][c] == 0:
            c += 1
        elif matrix[r][c] == '*':
            return False
        else:
            r, c = matrix[r][c]

    return False

print(solution(3,3,[[2,1]],[[0,1,2,0]]))