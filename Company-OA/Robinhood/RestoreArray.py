"""  
You had an array a of length n containing integer numbers with no repetitions, but it's been corrupted. You have a 
list of all the pairs of numbers that were adjacent to each other in a, so you might be able to restore it.

You are given pairs, an array of n-1 elements, where pairs[i] is a 2-element array of elements from a,
either in the form [a[j],a[j-1]] or [a[j+1], a[j]] for same j. Your task was to restore array a.

Example:
Input: pairs=[[3,5],[1,4],[2,4],[1,5]]
return: [3,5,1,4,2] or [2,4,1,5,3]
"""
from typing import List
from collections import defaultdict

"""  
very basic graph problem. Just take the pairs as edges and do dfs from the node which as degree 1.
"""
def solution(pairs: List[List[int]]) -> List[int]:
    if not pairs or not pairs[0]: return []

    n = len(pairs) + 1
    # hashmap for adjacency list
    m = defaultdict(list)
    # corner will always be size 2, to record the first and last element of the original list
    corner = []

    for p in pairs:
        a, b = p[0], p[1]
        m[a].append(b)
        m[b].append(a)

        if a in corner:
            corner.remove(a)
        else: 
            corner.append(a)

        if b in corner:
            corner.remove(b)
        else: 
            corner.append(b)
    
    res = [0] * n
    res[0], res[n-1] = corner[0], corner[1]

    i, j = 0, n-1

    while i < j:
        res[i+1] = m[res[i]][0]
        res[j-1] = m[res[j]][0]

        # update the neighbors list of adjacent elements
        m[res[i+1]].remove(res[i])
        m[res[j-1]].remove(res[j])

        i += 1
        j -= 1

    return res

pairs=[[3,5],[1,4],[2,4],[1,5]]
print(solution(pairs))


