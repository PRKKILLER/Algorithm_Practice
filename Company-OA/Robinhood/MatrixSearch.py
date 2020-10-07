"""  
给定 n, m, 想象构建 n * m 的矩阵 M: M[i,j] = (i+1)*(j+1)，0-based
​​​​​​​​​​​​​​​​​​​一系列query，有三种类型，第一种是查询矩阵中最小的元素，第二、三分别是禁用某一行、列
当某一列的最小值被禁用后，就不能用了
"""

class Solution:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.ban_row = set()
        self.ban_col = set()

    def queryMin(self):
        min_num = float('inf')

        for i in range(self.m):
            if i in self.ban_row:
                continue
            for j in range(self.n):
                if j in self.ban_col:
                    continue
                if ((i+1) * (j+1) < min_num):
                    min = (i+1) * (j+1)
        
        return min_num

    def Ban_row(self, r):
        self.ban_row.add(r)
    
    def Ban_col(self, c):
        self.ban_col.add(c)