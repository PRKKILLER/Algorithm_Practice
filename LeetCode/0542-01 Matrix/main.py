"""  
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
"""


class Solution:
    """  
    思路： BFS
    首先将所有 = 0 的 cell 入队，然后通过 BFS 的方法动态的更新当前已经入队的 cell 周围 = 1 的 cell 的值

    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque

        m, n = len(mat), len(mat[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        dq = deque([])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited[i][j] = True
                    dq.append((i, j))

        while dq:
            x, y = dq.popleft()
            for dx, dy in dirs:
                r, c = x + dx, y + dy
                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    mat[r][c] = mat[x][y] + 1
                    visited[r][c] = True
                    dq.append((r, c))

        return mat
