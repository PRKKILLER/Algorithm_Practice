"""  
给定1个n*n的matrix, 这个矩阵会有层层边框，螺旋向内。
对这个矩阵中边框上的数字进行排序，然后再按照顺时针的顺序重新排在边框上

Example:
Input: [[1,4],[2,3]]
Output: [[1,2],[3,4]]
"""

import heapq

def solution(matrix):
    m, n = len(matrix), len(matrix[0])
    tmp = []

    r_start, r_end = 0, m - 1
    c_start, c_end = 0, n - 1

    while r_start <= r_end and c_start <= c_end:
        pq = []

        # 处理只有1列的情况
        if (c_start == c_end):
            for i in range(r_start, r_end + 1):
                heapq.heappush(pq, matrix[i][c_start])
            tmp.append(pq)
            break

        # 处理只有1行的情况
        if (r_start == r_end):
            for i in range(c_start, c_end + 1):
                heapq.heappush(pq, matrix[r_start][i])
            tmp.append(pq)
            break

        for j in range(c_start, c_end + 1):
            heapq.heappush(pq, matrix[r_start][j])
        for i in range(r_start + 1, r_end + 1):
            heapq.heappush(pq, matrix[i][c_end])
        for j in range(c_end - 1, c_start - 1, -1):
            heapq.heappush(pq, matrix[r_end][j])
        for i in range(r_end - 1, r_start, -1):
            heapq.heappush(pq, matrix[i][c_start])
        
        tmp.append(pq)
        r_start += 1
        r_end -= 1
        c_start += 1
        c_end -= 1

    r_start, r_end = 0, m - 1
    c_start, c_end = 0, n - 1

    tmp = iter(tmp)
    while r_start <= r_end and c_start <= c_end:
        pq = next(tmp)
        for j in range(c_start, c_end + 1):
            matrix[r_start][j] = heapq.heappop(pq)
        for i in range(c_start + 1, c_end + 1):
            matrix[i][c_end] = heapq.heappop(pq)
        for j in range(c_end - 1, c_start - 1, -1):
            matrix[r_end][j] = heapq.heappop(pq)
        for i in range(r_end - 1, r_start, -1):
            matrix[i][c_start] = heapq.heappop(pq)

        r_start += 1
        r_end -= 1
        c_start += 1
        c_end -= 1

m = [
 [ 1, 2, 3 ],
 [ 8, 4, 9 ],
 [ 6, 7, 5 ]
]
solution(m)
print(m)