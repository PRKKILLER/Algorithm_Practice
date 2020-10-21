"""  
Given a 2-d array of "sharpness" values. 
Find a path from the leftmost column to the rightmost column which has the highest minimum sharpness.
Output the highest minimum sharpness. 
Each move can only move to the top right, right or bottom right grid.
Example: 3*3 matrix
5 7 2
7 5 8
9 1 5
The path with highest minimum sharpness is 7-->7-->8, because 7 is the highest minimum value 
in all the paths.
Idea: Use DP dp[r][c] = min(max(dp[r-1][c-1], dp[r][c-1], dp[r+1][c-1]), grid[r][c])

从最左一列中的任意一个出发，到达最右一列的任意一个，要求：
1）当前格子要想往右走，只能往右上、右边、右下三个格子移动；
2）一条path中最小的那个值才是这条path的合格value；-google 1point3acres
3）在所有path中找到合格value最大的那一条，输出它的value
"""
from typing import List

def highestMinValue(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        dp[i][0] = grid[i][0]

    for c in range(1, n):
        for r in range(1, m):
            col_max = 0
            for i in range(max(0, r - 1), min(m-1, r+1)+1):
                col_max = max(col_max, grid[i][c-1])
            dp[r][c] = min(col_max, grid[r][c])

    res = max(dp[r][n-1] for r in range(m))

    return res


grid = [
    [5,7,2],
	[7,5,8],
	[9,1,5]
]

print(highestMinValue(grid))


"""  
Follow up questions:
1. What if the grid is too big to store in the memory, how can you improve this algorithm

思路1： 
因为dp实际上只用到了当前列的前一列，因此可以改用1维数组，只保存当前列的前一列的值
缺点：因为文件特别大，每次只读取文件的每一行的第1个字符非常耗时，因为需要不断改变文件的指针 fpt

改进：可以考虑将当前文件的内容进行转置，然后存一个临时文件，然后这样该函数就变成了按行读取。
至于怎样对当前文件进行转置，可以根据内存大小每次先读几列，依次进行转置

缺点：读行输出列：写文件非常耗时；读列输出行：读文件非常耗时

最优解法： 根据内存大小读取一个接近正方形的矩形，将它写到新文件。然后再读取下一个矩形，这样就能使得读写次数最小
"""