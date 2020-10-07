//
// Created by 薛智钧 on 2020/3/24.
//

#include <iostream>
#include <vector>
using namespace std;

/*
 * Given an array nums with n integers, your task is to check if it could become
 * non-decreasing by modifying at most 1 element.

   We define an array is non-decreasing if nums[i] <= nums[i + 1] holds
   for every i (0-based) such that (0 <= i <= n - 2).

   Example 1:

  Input: nums = [4,2,3]
  Output: true
  Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
 * */

class Solution {
    // 该题要分情况讨论，讨论当前数字与前前数字(index - 2)之间的关系
    // 情况1: 4，[2],3 此时[2]的前前数字不存在，则修改前一个数字使其等于当前数字，即变为: 2, 2, 3
    // 情况2：3,4,[2],5 此时[2]的前前数字大于当前数字，则修改当前数字使其等于前一个数字，即4
    // 情况3：-1, 4, [2], 5 此时[2]的前前数字存在且小于（或等于）当前数字，则修改前一个数字，使其等于当前数字，
    // 即变为: -1, 2, 2, 5
public:
    bool checkPossibility(vector<int>& nums) {
        if (nums.size() < 2) return true;
        int cnt = 0;
        for (size_t i = 1; i < nums.size(); ++i){
            if (nums[i] < nums[i - 1]){
                if (cnt == 1) return false; // 若已经改变了一次，则返回false
                if (i == 1 || nums[i] >= nums[i - 2])
                    nums[i - 1] = nums[i];
                else                       // 这里必须要用else，因为上一个判断可能已对数组做出改变
                    nums[i] = nums[i - 1];
                ++cnt;
            }
        }
        return true;
    }

};

int main(){
    vector<int> nums = {4,2,1};
    Solution sol;
    cout << "Result: "<< sol.checkPossibility(nums);
}
