"""  
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        clockwise rotate
         * first reverse up to down, then swap the symmetry 
         * 1 2 3     7 8 9     7 4 1
         * 4 5 6  => 4 5 6  => 8 5 2
         * 7 8 9     1 2 3     9 6 3
        """
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def anti_rotate(self, matrix: List[List[int]]) -> None:
        """  
        anti-clockwise rotate
         * first swap the symmetry, and then reverse up to down 
         * 1 2 3     1 4 7     3 6 9 
         * 4 5 6  => 2 5 8  => 8 5 2
         * 7 8 9     3 6 9     1 4 7
        """

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        matrix.reverse()
