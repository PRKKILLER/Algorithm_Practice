"""  
每各员工都有一个0/1string， 代表其会不会与另外的人有交流。比如，如果0号员工的string是"100101"，意思就是说，
0号员工与0（自己），3，5号员工会有交流。
这个特征是有传递性的，也就是说，如果0和3有交流，3和9有交流，那么0和9就间接通过3有了交流。

给定一个邻接矩阵，举个例子 input: {"1011", "0100", "1010", "1001"}，返回小组的个数
"""

from typing import List

def solution(related: List[str]) -> int:
    related = [[int(c) for c in s] for s in related]
    n, cnt = len(related), 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(related, visited, i, n)
            cnt += 1
    
    return cnt

def dfs(related, visited, person, n):
    for other in range(n):
        if related[person][other] == 1 and not visited[other]:
            visited[other] = True
            dfs(related, visited, other, n)



related = ['110','110','001']
print(solution(related))
