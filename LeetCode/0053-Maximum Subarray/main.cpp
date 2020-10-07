//
// Created by 薛智钧 on 2020/3/27.
//
#include <vector>
#include <iostream>
#include <cstddef>
using namespace std;

/*
 * Given an integer array nums,
 * find the contiguous subarray (containing at least one number)
 * which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
 * */

/*
 * 定义两个变量 res 和 curSum，其中 res 保存最终要返回的结果，即最大的子数组之和，curSum 初始值为0，
 * 每遍历一个数字 num，比较 curSum + num 和 num 中的较大值存入 curSum，
 * 然后再把 res 和 curSum 中的较大值存入 res，以此类推直到遍历完整个数组，可得到最大子数组的值存在 res 中，代码如下：
 * */
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_global = INT_MIN, max_local = 0;
        for (int num : nums){
            // 将当前数字和（当前数字＋之前subArray的和）比大小
            // 若当前数字较大，则变更滑动窗口变更为当前数字为起点
            max_local = max(max_local + num, num);
            max_global = max(max_global, max_local);
        }
        return max_global;
    }
};

