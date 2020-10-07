//
// Created by 薛智钧 on 2020/3/24.
//

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;


/*
 * Given an array of integers and an integer k,
 * find out whether there are two distinct indices i and j in the array
 * such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
 *
 * 找到数组中是否存在两个下标i和j，使a[i] == a[j]，并且 |i - j| <= k
 * 注意是只要存在就行，不用都满足，因为相同的数字可能大于两个
 * */
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k < 1 && nums.size() < 2) return false;
        unordered_map<int, int>dict;
        for (int i = 0; i < nums.size(); ++i){
            if (dict.find(nums[i]) != dict.end() && (i - dict[nums[i]] <= k))
                return true;
            dict[nums[i]] = i;
        }
        return false;
    }
};
