//
// Created by 薛智钧 on 2020/5/31.
//
#include <iostream>
#include <vector>
using namespace std;

/*
 *  A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time.
    The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

    Now consider if some obstacles are added to the grids. How many unique paths would there be?

    An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
 * */

class Solution {
public:
    static int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        /* 初始化dp数组 */
        vector<vector<int>> dp(m, vector<int>(n, 0)); // 先全部初始为0
        int i = 0, j = 0;
        // 处理obstacles在map边界的情况
        for (; i < m; ++i) {
            if (obstacleGrid[i][0])
                break;
            dp[i][0] = 1;
        }
        for (; j < n; ++j) {
            if (obstacleGrid[0][j])
                break;
            dp[0][j] = 1;
        }
        // 开始正式dp计算
        for (i = 1; i < m; ++i) {
            for (j = 1; j < n; ++j) {
                if (!obstacleGrid[i][j])
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
            }
        }
        return dp[m - 1][n - 1];
    }

    // 对grid图左侧和上侧进行padding，同意边界情况
    // padding后的dp: dp[m+1][n+1]，其中dp[1][1]代表obstacleGrid中的[0][0]
     static int uniquePathsWithObstacles_2(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        dp[0][1] = 1; // 使得到达dp[1][1]=1
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (!obstacleGrid[i - 1][j - 1])
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
            }
        }
        return dp[m][n];
    }
};

int main() {
    vector<vector<int>> vec(1, vector<int>(1, 0));
//    vec[1][1] = 1;
    cout << Solution::uniquePathsWithObstacles(vec);
}
