//
// Created by 薛智钧 on 2020/4/8.
//
#include <vector>
#include <numeric>
using namespace std;

/*
 *  Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
 *  find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
 * */

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = (int)nums.size();
        return ((1 + n) * n / 2 - accumulate(nums.begin(), nums.end(), 0));
    }
};

