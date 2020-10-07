"""  
// 给数组内的所有数字按频率排序然后从右下角交错输出，频率相等就按大小排。
//例子:
//[[2,2,3],
//[1,1,1],
//[2,2,4]]
//
//按频率排序结果:
//[3,4,1,1,1,2,2,2,2]
//
//输出的时候从右下斜着填 (先填m[2][2], 然后m[2][1],然后m[1][2], 然后m[2][0], 然后[1][1] .... 最后m[0][0])
//[[2,2,2],
//[2,1,1],
//[1,4,3]]
"""
from collections import Counter

def solution(arr):
    tmp = [x for row in arr for x in row]
    c = list(dict(Counter(tmp)).items())
    c = sorted(c, key=lambda x: (x[1], x[0]))

    flattened = []
    for item in c:
        flattened += [item[0]] * item[1]
    
    idx = 0
    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr[0])-1, -1, -1):
            arr[i][j] = flattened[idx]
            idx += 1

    return arr

a = [[2,2,3],
     [1,1,1],
     [2,2,4]]

print(solution(a))