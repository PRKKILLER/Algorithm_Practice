"""  
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) 
and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix 
inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

dp[i+1][j+1] = area of square from points [0,0] to [i,j]
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # calculate prefix_sum matrix
        # dp[i][j] = area from point[0,0] to [i,j]
        for i in range(m):
            for j in range(n):
                self.dp[i + 1][j + 1] = matrix[i][j] + \
                    self.dp[i + 1][j] + self.dp[i][j + 1] - self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]
