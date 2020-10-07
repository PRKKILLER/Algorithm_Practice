"""  
You are given operations, an array containing the following 2 types of oprs:
1. [0,a,b]: create and save a rectangle of size a * b
2. [1,a,b]: answer the question: Could every one of the saved rectangles fit in a box of size a * b.
It is possible to rotate rectangles by 90 degrees.

Note: we are trying to fit each rectangles within the box separately (not all at the same time)

Return an array of booleans, representing the answers to the second type of operation, in the order 
they appear

Example:
operatons=[[0,1,3],[0,4,2],[1,3,4],[1,3,2]]
return: [true, false]
"""

def solution(operations):
    size_0, size_1 = 0, 0
    for ops in operations:
        if ops[0] == 0:
            size_0 += 1
        else:
            size_1 += 1

    if size_0 == 0 and size_1 != 0:
        return [True] * size_1

    res = [None] * size_1
    
    idx = 0
    max_len, max_wid = 0, 0
    size_0, size_1 = 0, 0

    for ops in operations:
        length, width = max(ops[1:]), min(ops[1:])
        if ops[0] == 0:
            max_len = max(max_len, length)
            max_wid = max(max_wid, width)
            size_0 += 1
        else:
            if size_0 == 0 and size_1 != 0:
                res[idx] = True
            elif length >= max_len and width >= max_wid:
                res[idx] = True
            else:
                res[idx] = False
            idx += 1
            size_1 += 1

    return res


operatons=[[0,1,3],[0,4,2],[1,3,4],[1,3,2]]
print(solution(operatons))
