//
// Created by 薛智钧 on 2020/3/17.
//

#include <iostream>
#include <vector>
using namespace std;

// Given an array of integers nums sorted in ascending order,
// find the starting and ending position of a given target value.
// Your algorithm's runtime complexity must be in the order of O(log n).
// If the target is not found in the array, return [-1, -1].

class Solution {
public:
    // 并不是严格的o(logn)
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.empty()) return {-1, -1};
        int end = binSearch_max(nums, target, 0, nums.size());
        if (end == -1) return {-1, -1};
        int start = end;
        for (; -1 < start; --start) {
            if (nums[start] < target)
                break;
        }
        return {start + 1, end};
    }

    vector<int> searchRange_2(vector<int>& nums, int target){
        if (nums.empty()) return {-1, -1};
        int end = binSearch_max(nums, target, 0, nums.size());
        if (end == -1) return {-1 , -1};
        int start = binSearch_min(nums, target, 0, nums.size());
        return {start, end};
    }

    // 返回命中元素最大的秩；若找不到，则返回-1
    int binSearch_max(vector<int>& nums, int target, int lo, int hi){
        while (1 < hi - lo){
            int mi = lo + (hi - lo) / 2; // 更安全，不会越界
            target < nums[mi] ? hi = mi : lo = mi; //[l0, mi) or [mi, hi)
        }
        return nums[lo] == target ? lo : -1;
    }

    // 返回命中元素最小的秩；若找不到，则返回-1
    int binSearch_min(vector<int>& nums, int target, int lo, int hi){
        while (lo < hi){
            int mi = lo + (hi - lo) / 2; // 更安全，不会越界
            target <= nums[mi] ? hi = mi : lo = mi + 1;
        }
        return nums[lo] == target ? lo : -1;
    }
};

int main(){
    vector<int> vec = {5,7,7,8,8,10};
    int target = 4;
    Solution sol;
    vector<int> res = sol.searchRange_2(vec, target);
    cout << "The begin and ending positions of target in the array are: ";
    for (int pos:res)
        cout << pos << ",";
}