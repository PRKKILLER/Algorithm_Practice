//
// Created by 薛智钧 on 2020/3/17.
//

#include <iostream>
#include <vector>
using namespace std;

// Given a sorted array and a target value, return the index if the target is found.
// If not, return the index where it would be if it were inserted in order.
// You may assume no duplicates in the array.

class Solution {
public:
    static int searchInsert_1(vector<int>& nums, int target) {
        if (nums.empty()) return 0;
        int index = 0;
        for (; index < nums.size(); ++index){
            if (target <= nums[index])
                break;
        }
        return index;
    }
    static int searchInsert(vector<int>& nums, int target) {
        if (nums.back() < target) return nums.size();
        int lo = 0, hi = nums.size();
        while (lo < hi) {
            int mi = lo + (hi - lo) / 2;
            nums[mi] < target ? lo = mi + 1: hi = mi;
        }
        return lo; // return的时候，lo=hi
    }
};

int main(){
    vector<int> vec = {1,3,5,6};
    int target = 5;
    cout << "The insert position is: " << Solution::searchInsert(vec, target);
}