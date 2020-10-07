from typing import List, Dict

def solution(matrix: List[List[int]]) -> List[bool]:
    def isFull(d: Dict):
        return all([x[1] == 1 for x in d.items()])
    
    m, n = 3, len(matrix[0])
    res = []
    d = {x: 0 for x in range(1, 10)}

    # initialize the d
    for i in range(m):
        for j in range(m):
            d[matrix[i][j]] += 1
    
    for j in range(n - 2):
        res.append(isFull(d))
        # 减去第一列
        for i in range(m):
            d[matrix[i][j]] -= 1
        
        if j+1 < n-2:
            # 加上新的一列
            for i in range(m):
                d[matrix[i][j+3]] += 1
    
    return res

mat = [[1, 2, 3, 2, 5, 7],
       [4, 5, 6, 1, 7, 6],
       [7, 8, 9, 4, 8, 3]]
    
print(solution(mat))

