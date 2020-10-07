//
// Created by 薛智钧 on 2020/5/28.
//
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
 *  Given a list of non-negative numbers and a target integer k,
 *  write a function to check if the array has a continuous subarray of size at least 2
 *  that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 * */

class Solution {
public:
    static bool checkSubarraySum(vector<int>& nums, int k) {
        // 键为 preSum % k, 值为索引
        unordered_map<int, int> mod_map{{0, -1}};
        auto preSum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            preSum += nums[i];
            // 若k = 0，则我们不能对k取模，而是在mod_map中寻找是否存在 preSum[index] = preSum[i]
            // 则 nums[i] - nums[index] = 0
            int tmp = k == 0 ? preSum : preSum % k;
            if (mod_map.count(tmp)) { // mod_map 存在相同的键
                if (i - mod_map[tmp] > 1) // subarray要求长度至少为2
                    return true;
                continue; // 如果子数组长度少于2， 不需要更新索引值
            }
            mod_map[tmp] = i; // 若tmp不存在，则存入mod_map
        }
        return false;
    }
};

int main(){
    vector<int> vec = {23, 2, 4, 6, 7};
    cout << Solution::checkSubarraySum(vec, 6);
}

