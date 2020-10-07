#include <iostream>
#include <vector>
using namespace std;

//
// Created by 薛智钧 on 2020/3/17.
//

// Given a sorted array nums,
// remove the duplicates in-place such that each element appear only once and return the new length.
// Do not allocate extra space for another array,
// you must do this by modifying the input array in-place with O(1) extra memory.

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int i=0, j = 0;
        while (++j < nums.size()){
            if (nums[j] != nums[i])
                nums[++i] = nums[j];
        }
        return i + 1;
    }
};

int main(){
    vector<int> vec = {0};
    Solution sol;
    int res = sol.removeDuplicates(vec);
    cout << "The remaining length is :" << res << endl;
    for (int i = 0; i < res; ++i)
        cout << vec[i] << ",";
}