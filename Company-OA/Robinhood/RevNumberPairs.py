"""  
Given an array of non-negative integers arr, your task is to count the number of pairs(i,j) such that
i <= j and arr[i] + rev(arr[j]) = arr[j]+ rev(arr[i])

对原表达式变形，即计算满足以下表达式的(i,j)数目：
arr[i]-rev(arr[i]) = arr[j]-rev(arr[j])

对于每个index i, 计算 fi = arr[i] - rev(arr[i])

suppose our fi array has 1 element with any (x) value ({x}), Only possible pair (i,j) for this case {0,0}. 
Total count is 1.
suppose our fi array has 2 elements with any (x) value ({x,x}), Possible pairs for this case {0,0}, {0,1}, {1,1}. 
Total count is 3.
suppose our fi array has 3 elements with any (x) value ({x,x,x}), Possible pairs for this case {0,0}, {0,1}, {0,2}, {1,1}, {1,2}, {2,2}. 
Total count is 6.
suppose our fi array has 4 elements with any (x) value ({x,x,x,x}), Possible pairs for this case {0,0}, {0,1}, {0,2}, {0,3}, {1,1}, {1,2}, {1,3}, {2,2}, {2,3}, {3,3}. 
Total count is 10.

Which will produce n*(n+1)/2.
"""


from typing import List
from collections import defaultdict

def solution(arr: List[int]) -> int:
    res = 0
    dict = defaultdict(int)

    for num in arr:
        dict[num - rev(num)] += 1

    for d in dict.items():
        res += d[1] * (d[1] + 1) // 2
    
    return res

def rev(num):
    return int(str(num)[::-1])

arr = [1,20,2,11]
print(solution(arr))
