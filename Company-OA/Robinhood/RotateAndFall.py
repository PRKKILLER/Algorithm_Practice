"""  
Your are given a matrix of characters representing a big box. Each cell of the matrix contains one of 3 characters:
1. '.': the cell is empty
2. '*': the cell contains an obstacle
3. '#', the cell contains a small box

You decide to rotate the big box clockwise to see how the small boxes will fall under the gravity.
After rotating, each small box falls down until it lands on an obstacle, another small box, or the 
bottom of the big box.

Given box, a matrix representation of the big box, return the state of the box after rotating it clickwise.

Example:
box = [['#','#', '.','.','.','.','.']
       ['#','#', '#','.','.','.','.'],
       ['#','#', '#','.','.','#','.']]
"""

def solution(box):
    m, n = len(box), len(box[0])

    for row in box:
        end = n - 1
        for j in range(n-1, -1, -1):
            if row[j] == '#':
                row[j] = '.'
                row[end] = '#'
                end -= 1
            elif row[j] == '*':
                end = j - 1

    return rotate(box)

def rotate(matrix):
    n = len(matrix[0])
    return [list(reversed([row[i] for row in matrix])) for i in range(n)]


box = [['#','#', '.','.','.','.','.'],
       ['#','#', '#','.','.','.','.'],
       ['#','#', '#','.','.','#','.']]

print(solution(box))