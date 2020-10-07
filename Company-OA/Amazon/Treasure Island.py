"""  
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks 
and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. 
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from the top-left corner of the map and can move one block up, down, left or right at a time. 
The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. 
Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. 
You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. 
Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""
from typing import List

def solution(island: List[List[str]]) -> int:
    routes = []
    n, m = len(island), len(island[0])

    def dfs(x, y, steps):
        if 0 <= x < n and 0 <= y < m:
            if island[x][y] == 'O':
                island[x][y] = 'D'  # mark as visited
                dfs(x, y-1, steps+1)
                dfs(x+1, y, steps+1)
                dfs(x, y+1, steps+1)
                dfs(x-1, y, steps+1)
            elif island[x][y] == 'D':
                return
            elif island[x][y] == 'X':
                routes.append(steps)
        return

    dfs(0, 0, 0)
    return sorted(routes)[0] if routes else -1

# BFS solution using queue
# 找最短路径应该使用BFS
from collections import deque

def solution2(islands: List[List[str]]) -> int:
    if not islands or not islands[0]:
        return -1
    
    n, m = len(islands), len(islands[0])
    q = deque([((0, 0), 0)]) # ((x, y), step)
    
    while q:
        (x, y), step = q.popleft()

        # visit current node's neighbors
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m:
                if islands[new_x][new_y] == 'O':
                    islands[new_x][new_y] = 'D' # mark as visited
                    q.append(((new_x, new_y), step+1))
                elif islands[new_x][new_y] == 'X':
                    return step + 1
    
    return -1


islands = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

print(solution2(islands))