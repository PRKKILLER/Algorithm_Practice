"""  
Given a positive integer n, generate an n x n matrix filled with elements 
from 1 to n^2 in spiral order.

Example:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        start_row, end_row = 0, n - 1
        start_col, end_col = 0, n - 1
        num = 1
        dir = 0

        while num <= n ** 2:
            if dir == 0:  # right direction
                for c in range(start_col, end_col + 1):
                    res[start_row][c] = num
                    num += 1
                start_row += 1

            elif dir == 1:  # down direction
                for r in range(start_row, end_row + 1):
                    res[r][end_col] = num
                    num += 1
                end_col -= 1

            elif dir == 2:  # left direction
                for c in range(end_col, start_col - 1, -1):
                    res[end_row][c] = num
                    num += 1
                end_row -= 1

            elif dir == 3:
                for r in range(end_row, start_row - 1, -1):
                    res[r][start_col] = num
                    num += 1
                start_col += 1

            dir = (dir + 1) % 4

        return res
