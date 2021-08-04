"""  
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. 
Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  
It is guaranteed the answer exists.

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
"""

from collections import deque


class Solution:
    """  
    solution 1: use standard one-way BFS search
    """

    def minKnightMoves(self, x: int, y: int) -> int:
        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        dq = deque([(0, 0, 0)])
        visited = set([(0, 0)])

        while dq:
            r, c, steps = dq.popleft()
            if (r, c) == (x, y):
                return steps

            for dx, dy in offsets:
                new_x, new_y = r + dx, c + dy
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    dq.append((new_x, new_y, steps + 1))

        return -1

    """  
    Solution 2: Use bi-direction BFS search to cut the time complexity half
    FOr bi-direction BFS, we need to use hashmap to keep track the visited positions
    and moves
    """

    def minKnightMoves(self, x: int, y: int) -> int:
        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        odq = deque([(0, 0, 0)])
        ovisited = {(0, 0): 0}

        tdq = deque([(x, y, 0)])
        tvisited = {(x, y): 0}

        while True:
            ox, oy, ostep = odq.popleft()
            if (ox, oy) in tvisited:
                return ostep + tvisited[(ox, oy)]

            tx, ty, tstep = tdq.popleft()
            if (tx, ty) in ovisited:
                return tstep + ovisited[(tx, ty)]

            for dx, dy in offsets:
                new_ox, new_oy = ox + dx, oy + dy
                if (new_ox, new_oy) not in ovisited:
                    ovisited[(new_ox, new_oy)] = ostep + 1
                    odq.append((new_ox, new_oy, ostep + 1))

                new_tx, new_ty = tx + dx, ty + dy
                if (new_tx, new_ty) not in tvisited:
                    tvisited[(new_tx, new_ty)] = tstep + 1
                    tdq.append((new_tx, new_ty, tstep + 1))
