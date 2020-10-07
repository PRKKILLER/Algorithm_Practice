//
// Created by 薛智钧 on 2020/4/6.
//
#include <iostream>
#include <vector>
using namespace std;

/*
 * Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 */

class Solution {
public:
    // 这道题和search in rotated sorted array唯一区别在于存在duplicates
    // eg. [1,1,3,1], [3,1,1].这两种情况，中间值 = 最右侧值时，target=3可能存在于左侧，或者右侧
    // 对于这种情况，只要把最右值向左一位即可继续循环，如果还相同则继续移，直到移到不同值为止
    bool search(vector<int>& nums, int target) {
        int lo = 0, hi = nums.size() - 1;
        while (lo <= hi){
            int mi = lo + (hi - lo) / 2;
            if (nums[mi] == target) return true;
            if (nums[mi] < nums[hi]){ // 右侧有序
                if (nums[mi] < target && nums[hi] >= target) lo = mi + 1;
                else hi = mi - 1;
            }else if (nums[mi] > nums[hi]){ // 左侧有序
                if (nums[mi] > target && nums[lo] <= target) hi = mi - 1;
                else lo = mi + 1;
            }else{ // nums[lo] == nums[hi]
                --hi;
            }
        }
        return false;
    }
};

