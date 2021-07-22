"""  
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # the trick here is to realize that numbers that are on the same diagonal
        # the sum of their indices are equal

        # Note: Dictionaries preserve insertion order
        from collections import defaultdict

        d = defaultdict(list)
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                d[i + j].append(mat[i][j])

        res = []
        for k, v in d.items():
            if k % 2 == 0:
                res.extend(v[::-1])
            else:
                res.extend(v)

        return res
