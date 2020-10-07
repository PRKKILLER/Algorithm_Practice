//
// Created by 薛智钧 on 2020/4/8.
//
#include <vector>
using namespace std;

/*
 * Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
 * */

class Solution {
    // 翻转数组的本质：原来数字是有序的，但是翻转之后小的数字在大的数字之前
    // 用分而治之的方式，将原数组分成两部分，然后比较subarray的起始和结束
    // 只要arr[start] <= arr[end]，就说明该subarray有序，返回arr[start]
public:
    int findMin(vector<int>& nums) {
        return helper(nums, 0, (int)nums.size() - 1);
    }

    // 当mid = (lo + arr.size() -1) / 2来计算时，mid + 1 一定不会越界
    // 当mid = (lo + arr.size()) / 2计算时，mid + 1就可能越界
    static int helper(vector<int>& nums, int start, int end){
        if (nums[start] <= nums[end]) return nums[start];
        int mid = start + (end - start) / 2;
        return min(helper(nums, start, mid), helper(nums, mid + 1, end));
    }
};
