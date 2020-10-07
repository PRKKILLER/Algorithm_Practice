"""  
顺时针旋转矩阵k次，且diagonal 上的元素不装
"""

def solution(matrix, k):
    m, n = len(matrix), len(matrix[0])
    
    for _ in range(k):
        for i in range(m):
            for j in range(i+1, n):
                if i != j and i != n - 1 - j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(m):
            for j in range(n // 2):
                if i != j and i != n - 1 - j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(solution(matrix, 1))

