"""  
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row, end_row = 0, len(matrix) - 1
        start_col, end_col = 0, len(matrix[0]) - 1
        res = []
        dir = 0

        while start_row <= end_row and start_col <= end_col:
            if dir == 0:  # right direction
                for c in range(start_col, end_col + 1):
                    res.append(matrix[start_row][c])
                start_row += 1

            elif dir == 1:  # down direction
                for r in range(start_row, end_row + 1):
                    res.append(matrix[r][end_col])
                end_col -= 1

            elif dir == 2:  # left direction
                for c in range(end_col, start_col - 1, -1):
                    res.append(matrix[end_row][c])
                end_row -= 1

            elif dir == 3:  # up direction
                for r in range(end_row, start_row - 1, -1):
                    res.append(matrix[r][start_col])
                start_col += 1

            dir = (dir + 1) % 4

        return res
