//
// Created by 薛智钧 on 2020/5/29.
//
#include <iostream>
#include <vector>
using namespace std;

/*
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
 * That means the first house is the neighbor of the last one.
 * Meanwhile, adjacent houses have security system connected and it will automatically contact the police
 * if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
 determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
 * */

class Solution {
public:
    // 思路：因为House[1]和House[n]是相邻的，所以并不能同时抢
    // 于是问题就变成 a) 抢House[1] ~ House[n-1]; b) 抢House[2] ~ House[n]
    // 这两个子问题又变成了基础的 House Robber问题
    static int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];
        int maxSum = 0;
        for (int i = 0; i < 2; ++i) {
            int prev1 = 0, prev2 = 0;
            // 搜索 house[1] ~ house[n-1] 或 house[2] ~ house[n]
            int flag = i == 0 ? 1 : 0;
            for (int j = i; j < nums.size() - flag; ++j) {
                int tmp = prev1;
                prev1 = max(prev2 + nums[j], prev1);
                prev2 = tmp;
            }
            maxSum = max(prev1, maxSum);
        }
        return maxSum;
    }
};

int main() {
    vector<int> vec = {3,1};
    cout << Solution::rob(vec);
}