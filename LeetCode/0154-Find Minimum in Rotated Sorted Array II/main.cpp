//
// Created by 薛智钧 on 2020/4/8.
//
#include <vector>
using namespace std;

/*
 * Suppose an array sorted in ascending order
   is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [5,3,5]
Output: 3
 * */

class Solution {
public:
    // 这题与find minimum in rotated sorted array的区别
    // 在于存在重复元素，因此当arr[start] == arr[end]时，序列不一定有序
    // 只有当arr[start] < arr[end]，序列才一定有序
    int findMin(vector<int>& nums) {
        return helper(nums, 0, (int)nums.size() - 1);
    }

    static int helper(vector<int>& nums, int lo, int hi){
        if (lo == hi) return nums[lo]; // 当子序列只存在一个元素时，返回
        if (nums[lo] < nums[hi]) return nums[lo];
        int mi = lo + (hi - lo) / 2;
        return min(helper(nums, lo, mi), helper(nums, mi + 1, hi));
    }
};
