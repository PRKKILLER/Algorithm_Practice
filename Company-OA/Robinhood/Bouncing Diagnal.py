def bouncingDiagonals(matrix):
    res = []
    
    m = len(matrix)
    top = 0
    
    for i in range(m):
        top += matrix[i][i]
    
    res.append([top, matrix[0][0]])
    
    for idx in range(1, m):
        tmp = 0
        i, j = idx, 0
        while i >= 0 and j < m:
            tmp += matrix[i][j]
            i -= 1
            j += 1
        
        i, j = 0, idx
        while i < m and j < m:
            tmp += matrix[i][j]
            i += 1
            j += 1
        
        tmp -= matrix[0][idx]
        res.append([tmp, matrix[idx][0]])
    
    res = sorted(res, key=lambda x: (x[0], x[1]))
    return [x[1] for x in res]

matrix = [[2,3,2], 
 [0,2,5], 
 [1,0,1]]

print(bouncingDiagonals(matrix))