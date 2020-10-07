//
// Created by 薛智钧 on 2020/4/7.
//
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
 * Given an array nums of n integers and an integer target,
 * find three integers in nums such that the sum is closest to target.
 * Return the sum of the three integers.
 * You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 * */

class Solution {
public:
    // 因为题意说明了只有一个解，因此不用考虑重复的情况
    // 利用两个指针滑动寻找另外两个数
    int threeSumClosest(vector<int>& nums, int target) {
        int closestSum = nums[0] + nums[1] + nums[2];
        if (closestSum == target)
            return target;
        sort(nums.begin(), nums.end()); // 先排序
        int minDiff = abs(closestSum - target); // 记录3数之和与target的最小差
        for (int k = 0; k < (int)nums.size() - 2; ++k){
            int lo = k + 1, hi = (int)nums.size() - 1;
            while (lo < hi){
                int curSum = nums[k] + nums[lo] + nums[hi];
                if (curSum == target)
                    return target;
                int curDiff = abs(curSum - target);
                if (curDiff < minDiff) {
                    minDiff = curDiff;
                    closestSum = curSum;
                }
                if (curSum < target) ++lo;
                else  --hi;
            }
        }
        return closestSum;
    }
};

int main(){
    int target = 1;
    vector<int> arr = {-1, 2, 1, -4};
    Solution sol;
    cout << sol.threeSumClosest(arr, target);
}