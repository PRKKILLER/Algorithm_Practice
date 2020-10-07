"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        res = [[1]]
        for i in range(1, numRows):
            row = [x+y for x, y in zip([0]+res[i-1], res[i-1]+[0])]
            res.append(row)
        
        return res


    def generate2(self, numRows: int) -> List[list[int]]:
        if not numRows:
            return []
        
        res = [[1]]
        for i in range(2, numRows):
            row = [0] * i
            row[0] = row[i-1] = 1
            for j in range(1, i - 1):
                row[j] = res[i-2][j] + row[i-2][j-1]
            
            res.append(row)
        
        return res