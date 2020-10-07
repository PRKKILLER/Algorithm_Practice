"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res = [x + y for x, y in zip([0] + res, res + [0])]

        return res

    """
    e.g.: res=[1,2,1]
    [0]+res=[0,1,2,1]
    res+[0]=[1,2,1,0]
    zip([0]+res,res+[0])=[(0,1),(1,2),(2,1),(1,0)]
    """

    def getRow2(self, rowIndex: int) -> List[int]:
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                res[j] += res[j - 1]
        
        return res
