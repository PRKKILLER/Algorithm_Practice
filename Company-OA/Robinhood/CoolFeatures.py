"""  
With 2 arrays a and b, the 2 types of queries are as follows:
1. If the query is of the form [0,i,x], then b[i] should be assigned the value of x
2. If the query is of the form [1,x], then find the total number of pairs indices i and j such that 
a[i] + b[j] = x

Given a, b and array of queries, return an array of the results of the queries of the second

Example:
a=[1,2,3],b=[3,4], and query=[[1,5],[0,0,1],[1,5]]
Output: [2,1]
"""
from typing import List
from collections import defaultdict

def solution2(a: List[int], b: List[int], query) -> List[int]:
    if not a or not b or not query:
        return []

    res = []
    map_a, map_b = defaultdict(int), defaultdict(int)

    for num in a:
        map_a[num] += 1

    for num in b:
        map_b[num] += 1

    for q in query:
        if q[0] == 0:
            old_val = b[q[1]]
            map_b[old_val] -= 1
            map_b[q[2]] += 1
        else:
            cnt = 0
            for k in map_a:
                if q[1] - k in map_b:
                    cnt += map_a[k] * map_b[q[1] - k]
            res.append(cnt)
    
    return res

#该方法会TLE
def solution(a: List[int], b: List[int], query) -> List[int]:
    n, m = len(a), len(b)
    res = []
    for q in query:
        if q[0] == 0:
            b[q[1]] = q[2]
        else:
            cnt = 0
            if n < m:
                tmp = set(b)
                for elem in a:
                    if q[1] - elem in tmp:
                        cnt += 1
            else:
                tmp = set(a)
                for elem in b:
                    if q[1] - elem in tmp:
                        cnt += 1
                
            res.append(cnt)

    return res

a=[1,2,3]
b=[3,4]
query=[[1,5],[0,0,1],[1,5]]
print(solution2(a,b,query))