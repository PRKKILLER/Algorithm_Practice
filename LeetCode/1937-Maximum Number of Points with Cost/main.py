"""  
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the 
number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) 
will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. 
For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) 
will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.

Constraints:

m == points.length
n == points[r].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= points[r][c] <= 105
"""

"""
M: number of rows; N: number of columns

dp[i][j]: 表示当我们走到 points[i][j] 时， 所能得到的最大值

Before optimization:
dp[i][j] = max(dp[i-1][k], abs(j - k)) + points[i][j]
该情况下，对于每一个 points[i][j]，我们需要 O(N) 的时间得到dp[i][j]
则总时间复杂度为: O(M*N^2)

After optimization:
k<=j, k在j左边 => dp[i][j] =  points[i][j] - j + max{dp[i-1][k] + k}，此时因为 points[i][j] - j 是定值，因此只需要求得
max{dp[i-1][k] + k} where K <= j

k > j, k在j右边 => dp[i][j] =  points[i][j] + j + max{dp[i-1][k] - k}，此时因为 points[i][j] + j 是定值，因此只需要求得
max{dp[i-1][k] - k} where k in [j, n-1]

时间复杂度: O(M*N)
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev = [0] * n

        for i in range(m):
            cur = [0] * n

            # first round, when k <= j, max{dp[i-1][k] + k}中的k可取[0,j]
            best = float('-inf')
            for j in range(n):
                # equivalent as: max{dp[i-1][k] + k} where K <= j
                best = max(best, prev[j] + j)
                cur[j] = points[i][j] - j + best

            # second round, when k > j, max{dp[i-1][k] - k}中的k可取[j, n-1]
            best = float('-inf')
            for j in range(n - 1, -1, -1):
                # equivalent to max{dp[i-1][k] - k} where k in [j, n-1]
                best = max(best, prev[j] - j)
                cur[j] = max(cur[j], points[i][j] + j + best)

            prev = cur

        return max(prev)
