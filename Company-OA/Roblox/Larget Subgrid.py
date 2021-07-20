"""  
https://leetcode.com/discuss/interview-question/850974/hackerrank-online-assessment-roblox-new-grad-how-to-solve-this

You are given an integer square grid which can be divided into square sub-grids.

sub-grid sum is obtained by adding all elements of the sub-grid. Determine the maximum size of a square sub-grid such that all
sub-grids of this size must have sub-grid sum less than or equal to a given value (maxSum). 

Return the size of that sdub-grid
"""
from typing import List


def largestSubgrid(grid: List[List[int]], maxSum: int) -> int:
    if not grid or not grid[0]:
        return 0

    n = len(grid)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    mx = 0  # maximum grid cell

    # formulate prefixSum matrix
    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = grid[i][j] + \
                dp[i + 1][j] + dp[i][j + 1] - dp[i][j]
            mx = max(mx, grid[i][j])

    if maxSum < mx:
        return 0

    if maxSum == mx:
        return 1

    if maxSum >= dp[n][n]:
        return n

    def regionSum(row1, col1, row2, col2) -> int:
        return dp[row2][col2] - dp[row2][col1 - 1] - dp[row1 - 1][col2] + dp[row1 - 1][col1 - 1]

    lo, hi = 0, n
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid == 0:
            return 0

        if mid == 1 and mx < maxSum:
            ans = 1
            lo = mid + 1
            continue

        stop = False

        for i in range(mid, n + 1):
            if stop:
                break
            for j in range(mid, n + 1):
                subSum = regionSum(i - mid + 1, j - mid + 1, i, j)
                if subSum > maxSum:
                    stop = True
                    break

        if stop:
            hi = mid - 1
        else:
            res = mid
            lo = mid + 1

    return res


if __name__ == "__main__":
    grid = [[1, 1, 1] for _ in range(3)]
    maxSum = 4
    print(largestSubgrid(grid, 9))
