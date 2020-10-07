"""  
You are given a rectangular matrix "numbers" consisting positive integers, where cells are colored in the
black and white

Your task is to sort the numbers on the chess board according to a set of queries. each element of the query
is [x,y,w], representing a w*w submatrix with its upper-left corner at (x,y) on the "numbers" matrix

For each query, sort the number within the submatrix separately:
1. sort all the numbers on black squares within the submatrix in their relative order of ascending value
2. sort all the numbers on white squares within the submatrix in their relative order of ascending value
3. "numbers" should be re-arranged within the submatrix such that each number ends up on the same color square
that it started on.

Return "numbers" matrix after processing all the queries on it

注：
黑色方块的位置满足: (i+j) % 2 == 0;
白色方块的位置满足: (i+j) % 2 == 1
"""

import heapq as hq

def solution(matrix, queries):
    for q in queries:
        s_i, s_j = q[0], q[1]
        w = q[2]
        black, white = [], []
        for i in range(s_i, s_i + w):
            for j in range(s_j, s_j + w):
                if (i + j) % 2 == 0:
                    hq.heappush(black, matrix[i][j])
                else:
                    hq.heappush(white, matrix[i][j])

        for i in range(s_i, s_i + w):
            for j in range(s_j, s_j + w):
                if (i + j) % 2 == 0:
                    matrix[i][j] = hq.heappop(black)
                else:
                    matrix[i][j] = hq.heappop(white)
    
    return matrix