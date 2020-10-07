"""  
Given a square matrix of integers a and an array of queries q, your task is to return the given matrix
after processing all the queries on it. There are three types of querues:
1. q[i] = 0, rotate the matrix 90 degree clockwise
2. q[i] = 1, reflect the matrix in its main diagonal
3. q[i] = 2, reflect the matrix in its secondary diagonal

Example:
a = [[1,2,3],
    [4,5,6],
    [7,8,9]]

q = [0,1,2]

Output:
out = [[3,6,9],
       [2,5,8],
       [1,4,7]]
"""

# rotate matrix 90 degree clockwise
def rotate(matrix):
    res = [list(reversed([row[i] for row in matrix])) for i in range(len(matrix))]
    return res

def diagonalMain(matrix):
    res = [[row[i] for row in matrix] for i in range(len(matrix))]
    return res

def diagonalSecond(matrix):
    tmp = list(reversed(diagonalMain(matrix)))
    return [list(reversed(row)) for row in tmp]

def solution(a, queries):
    for q in queries:
        if q == 0:
            a = rotate(a)
        elif q == 1:
            a = diagonalMain(a)
        elif q == 2:
            a = diagonalSecond(a)
    
    return a

a = [[1,2,3],
    [4,5,6],
    [7,8,9]]

q = [0,1,2]

print(solution(a, q))