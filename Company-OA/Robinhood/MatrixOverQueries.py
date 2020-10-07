"""  
给一个array和一个matrix。 matrix里面每一个vector<int>的形式必定是[l,r,target]，固定只有3个数。 
要求统计array里 index从l 到 r这个区间出现了多少次target这个数。 

比如:
array = [1,1,2,3,2]
matrix = [[1,2,1],
          [2,4,2],
          [0,3,1]] 
output : 5

//因为在matrix[0], array的index 1到2区​​​​​​​​​​​​​​​​​​​间出现了1 一次， matrix[1], array的index 2到4区间出现2 两次。 
matrx[2], array的index 0到3区间出现1 两次
"""

from collections import defaultdict

def solution(arr, matrix):
    res = 0
    mapping = defaultdict(list)

    for row in matrix:
        mapping[row[2]].append((row[0], row[1]))
    
    for i, num in enumerate(arr):
        if num in mapping:
            for d in mapping[num]:
                if d[0] <= i <= d[1]:
                    res += 1

    return res

array = [1,1,2,3,2]
matrix = [[1,2,1],
          [2,4,2],
          [0,3,1]]
print(solution(array, matrix))