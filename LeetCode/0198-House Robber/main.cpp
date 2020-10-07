//
// Created by 薛智钧 on 2020/5/29.
//
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
 * 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
 * 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 * */


/*
 *  这是一个standard DP问题，而DP的问题一般可以分为以下几步：
 *  1. Find recursive relation
    2. Recursive (top-down)
    3. Recursive + memo (top-down)
    4. Iterative + memo (bottom-up)
    5. Iterative + N variables (bottom-up)

    1. 找出DP问题的状态转移方程：
    对于house[i]，小偷有2个选择：a) 偷现在的房子i b)不偷现在的房子i
    如果选择了方案a，则意味着house[i-1]不能偷，但是house[i-2]及其之前的房子可以去偷；
    如果选择了方案b，则意味着小偷了可以获得house[i-1]及其之前房子的所有可能情况
    因此可以得到以下的状态转移方程： rob(i) = max(rob(i-2) + current, rob(i-1))
 * */
class Solution {
public:
    /*Recursive: top-down*/
    int rob_1(vector<int>& nums) {
        return rob_1(nums, nums.size() - 1);
    }

    int rob_1(vector<int>& nums, int i) {
        if (i < 0) return 0;
        return max(rob_1(nums, i - 2) + nums[i], rob_1(nums, i - 1));
    }

    /*Recursive: top-down + memo*/
    int rob_2(vector<int>& nums) {
        vector<int> memo(nums.size(), -1);
        return rob_2(nums, memo, nums.size() - 1);
    }

    int rob_2(vector<int>& nums, vector<int>& memo, int i) {
        if (i < 0) return 0;
        if (memo[i] > -1) return memo[i];
        memo[i] = max(rob_2(nums, memo, i - 2) + nums[i], rob_2(nums, memo, i - 1));
        return memo[i];
    }

    /*Iterative + memo (bottom-up)*/
    int rob_3(vector<int> nums) {
        if (nums.empty()) return 0;
        vector<int> memo(nums.size() + 1, -1);
        memo[0] = 0, memo[1] = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            memo[i + 1] = max(memo[i - 1] + nums[i], memo[i]);
        }
        return memo.back();
    }

    /*iterative + N variables (bottom-up)*/
    // 可以注意到，我们在计算时仅仅用到了memo[i-2], memo[i-1]两个变量
    // 因此可以利用两个变量保存
    int rob(vector<int> nums) {
        if (nums.empty()) return 0;
        int prev1 = 0, prev2 = 0;
        for (int num : nums) {
            int tmp = prev1;
            prev1 = max(prev2 + num, prev1);
            prev2 = tmp;
        }
        return prev1;
    }
};

int main(){
    vector<int> vec = {2,1,1,2};
    Solution sol;
    cout << sol.rob_2(vec);
}
