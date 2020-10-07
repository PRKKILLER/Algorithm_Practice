//
// Created by 薛智钧 on 2020/3/28.
//
#include <iostream>
#include <vector>
using namespace std;
/*
 * You are climbing a stair case. It takes n steps to reach to the top.

   Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

   Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
 *
 * */
// 状态转移方程: f(n) = f(n-1) + f(n-2)
class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        vector<int> dp(n+1);
        dp[1] = 1; dp[2] = 2;
        for (int i = 3; i <= n; ++i) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }

    // 利用fibonacci 数列求解
    int climbStairs_2(int n){
        if (n == 1) return 1;
        int first = 1, second = 2;
        for (int i = 3; i <= n; ++i) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }

    int climbStairs_3(int n){
        if (n == 1) return 1;
        int f = 1, s = 2;
        for (int i = 3; i <= n; ++i) {
            s += f;
            f = s - f;
        }
        return s;
    }
};



