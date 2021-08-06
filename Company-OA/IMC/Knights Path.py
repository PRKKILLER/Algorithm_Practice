"""
Given a chess board of n rows ( top to bottom ) and n columns ( left to right ).
In each move, a knight moves either:
2 column positions and 1 row position 2 row positions an 1 column position

In other words, a move is 2 steps along one axis and 1 step along a perpendicular axis.
A bishop, on the other hand, moves any number of steps diagonaly.

Both the knight and bishop capture any piece that is on a position that it moves to.
A position that a piece can move to is said to be threatened by that piece,
because if another piece moves to that position , then it can be captured.


Given a starting position A and ending position B for the knight, and a bishop position C, calculate the minimum
number of moves needed by the knight to move from A to B while avoiding all positions threatened by the bishop.
If the knight captures the bishop on one of its moves, then it can move into positions
that were previously threatened by the bishop.

If there is no possible path to B, return -1. All moves must remain within the chess board.

Note: The knight may move to B even if B is threatened by the bishop.
"""

from typing import List

# bidirection BFS solution


def solution(n: int, A: List, B: List, C: List) -> int:
    from collections import deque

    def is_danger(x: int, y: int):
        return [x, y] != B and abs(x - C[0]) == abs(y - C[1])

    # the offsets in the eight directions
    offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
               (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

    odq = deque([(A[0], A[1], 0, True)])  # origin deque
    omp = {(A[0], A[1]): 0}  # origin map

    tdq = deque([(B[0], B[1], 0, True)])  # target deque
    tmp = {(B[0], B[1]): 0}  # target map

    while odq and tdq:
        ox, oy, osteps, oflag = odq.popleft()
        if (ox, oy) in tmp:
            return osteps + tmp[(ox, oy)]

        tx, ty, tsteps, tflag = tdq.popleft()
        if (tx, ty) in omp:
            return tsteps + omp[(tx, ty)]

        for dx, dy in offsets:
            new_ox, new_oy = ox + dx, oy + dy
            if oflag and [new_ox, new_oy] == C:
                oflag = False
            if oflag:
                if 0 <= new_ox < n and 0 <= new_oy < n and (not is_danger(new_ox, new_oy)) and (new_ox, new_oy) not in omp:
                    omp[(new_ox, new_oy)] = osteps + 1
                    odq.append((new_ox, new_oy, osteps + 1, True))
            else:
                if 0 <= new_ox < n and 0 <= new_oy < n and (new_ox, new_oy) not in omp:
                    omp[(new_ox, new_oy)] = osteps + 1
                    odq.append((new_ox, new_oy, osteps + 1, False))

            new_tx, new_ty = tx + dx, ty + dy
            if tflag and [new_tx, new_ty] == C:
                tflag = False
            if tflag:
                if 0 <= new_tx < n and 0 <= new_ty < n and (not is_danger(new_tx, new_ty)) and (new_tx, new_ty) not in tmp:
                    tmp[(new_tx, new_ty)] = tsteps + 1
                    tdq.append((new_tx, new_ty, tsteps + 1, True))
            else:
                if 0 <= new_tx < n and 0 <= new_ty < n and (new_tx, new_ty) not in tmp:
                    tmp[(new_tx, new_ty)] = tsteps + 1
                    tdq.append((new_tx, new_ty, tsteps + 1, False))

    return -1


print(solution(4, [0, 0], [1, 2], [-1, 2]))
