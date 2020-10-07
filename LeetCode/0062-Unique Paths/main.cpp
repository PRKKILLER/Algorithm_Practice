//
// Created by 薛智钧 on 2020/5/31.
//
#include <iostream>
#include <vector>
using namespace std;

/* A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

 The robot can only move either down or right at any point in time.
 The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
 *
 *
 *  Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
 * */

class Solution {
public:
    /* vanilla  DP solution:
     * 因为robot只能 向右 / 向下 走，因此当我们到达地图中的一个point时，它要么是从左侧到达的，要么是从上方到达的
     * 因此用dp[i][j]表示到达第(i, j)个方格的unique paths，则状态转移方程则变为：
     * dp[i][j] = dp[i-1][j] + dp[i][j-1]。
     * 除此以外，我们有base case: dp[0][j] = dp[i][0] = 1
     * */
    // time: O(m*n), space:O(m, n)
    static int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 1));
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }
    /*
     * 观察可知，计算过程中只是用到了dp[i-1][j](previous row)）和dp[i][j-1](current row)，
     * 因此，可以将memory usage降低到O(n)
     * */
    static int uniquePaths_2(int m, int n) {
        vector<int> pre(n, 1), cur(n, 1);
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                cur[j] = pre[j] + cur[j - 1];
            }
            swap(cur, pre); // 开始下一次循环前，令pre = cur
        }
        return pre[n - 1];
    }

    /* 利用排列组合直接得出结论
     * robot一开始的位置是(1, 1)， 因此不管采取什么样的路线，总共要走的步数都是：
     * steps = (m-1)+(n-1)=m+n-2，向下走m-1歩，向右走n-1歩
     * 因此总的unique paths数量就是从m+n-2歩中取出m-1歩的方法的总数量
     * */
    static int uniquePaths_3(int m, int n) {
        int N = n + m - 2;// how much steps we need to do
        int k = m - 1; // number of steps that need to go down
        double res = 1;
        // here we calculate the total possible path number
        // Combination(N, k) = n! / (k!(n - k)!)
        // reduce the numerator and denominator and get
        // C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!
        for (int i = 1; i <= k; i++)
            res = res * (N - k + i) / i;
        return (int)res;
    }
};

int main() {
    cout << Solution::uniquePaths_3(7, 3);
}