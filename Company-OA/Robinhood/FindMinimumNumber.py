"""  
题目是说，query里面的每个int[] -> 代表的是left & right。你要做的是，找到最小的number个数，使得它们都可以包含在所有的int[] 里面。

Example: Input: int[][] query = [ [-1,3], [-5,-3], [3,5], [2,4], [-3,-2], [-1,4], [5,5] ]; output: 3
比如：对于这个query来说，numbers: -3，3，5。所以，最小的Min number就是3。
"""

from typing import List

def solution(arr):
    if not arr: return 0

    arr = sorted(arr, key=lambda x: x[0])
    left, right = arr[0][0], arr[0][1]
    res = []

    for i in range(1, len(arr)):
        if arr[i][0] <= right:
            left = arr[i][0]
            right = min(right, arr[i][1])
        else:
            tmp = (left, right)
            res.append(tmp)
            left, right = arr[i][0], arr[i][1]
    
    tmp = (left, right)
    res.append(tmp)

    return res


query = [ [-1,3], [-5,-3], [3,5], [2,4], [-3,-2], [-1,4], [5,5] ]
print(solution(query))
