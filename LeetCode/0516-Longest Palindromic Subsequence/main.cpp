//
// Created by 薛智钧 on 2020/4/7.
//
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/*Given a string s, find the longest palindromic subsequence's length in s.
 * You may assume that the maximum length of s is 1000.

Example 1:
Input: "bbbab"
Output: 4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: "cbbd"
Output: 2
 */

class Solution {
public:
    // 有关极值的问题，首先要想到 贪心算法和dp
    // 构建一个2维的dp数组
    // dp[i][j] 保存区间[i, j]内的字符串的最长回文子序列

    int longestPalindromeSubseq(string s) {
        if (s.size() < 2) return s.size();

        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = n - 1; i >= 0; --i){ // 从最后一个元素扫描
            dp[i][i] = 1;
            for (int j = i + 1; j < n; ++j){
                if (s[i] == s[j])
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                else
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
        return dp[0][n - 1];
    }
};

