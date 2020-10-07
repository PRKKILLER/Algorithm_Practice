//
// Created by 薛智钧 on 2020/4/8.
//
#include <iostream>
#include <vector>
using namespace std;

/*
 *  Given an array nums, write a function to move all 0's to the
 *  end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

 * */

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0;
        for (int j = 1; j < nums.size(); ++j){
            if (nums[j])
                nums[i++] = nums[j];
        }
        while (i < nums.size())
            nums[i++] = 0;
    }
};
