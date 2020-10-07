"""  
根据input给的长度num，最小值，最大值，创建一个strictly increasing, then strictly decreasing的长度为num的list，
并且这个list是alphabetically最大的，e.g. 8,9,10,9,8,7 > 7,8,9,10,9。如果不存在，return -1。

Input:
num=5
lowerEnd=3
UpperEnd=10

Output:
[9,10,9,9,7]

Explanation:
In this case, [9,10,9,8,7] us the winning sequence. It maintains the constraints of being first strictly
increasing and then strictly decreasing, and there is no way to have integers in the sequence that are greater than
[9,10,9,8,7]

So the output is [9,10,9,8,7]
"""
from typing import List

def solution(num: int, lowerEnd: int, upperEnd: int) -> List[int]:
    if num < 3 or lowerEnd >= upperEnd:
        return -1
    
    ans = [0] * num

    if num <= upperEnd - lowerEnd + 2:
        ans[0] = upperEnd - 1
        ans[1] = upperEnd
        for i in range(2, num):
            ans[i] = ans[i-1] - 1
    elif num <= 2 * (upperEnd - lowerEnd) + 1:
        peak = num - 1 - (upperEnd - lowerEnd)
        ans[peak] = upperEnd
        i = peak - 1
        while i >= 0:
            ans[i] = ans[i+1] - 1
            i -= 1
        i = peak + 1
        i = peak + 1
        while i < num:
            ans[i] = ans[i-1] - 1
            i += 1
    else: # too long, impossible to get ans
        return -1
    
    return ans


