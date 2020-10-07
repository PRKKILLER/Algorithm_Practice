//
// Created by 薛智钧 on 2020/3/24.
//
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

/*
 * Given an array of integers, find if the array contains any duplicates.

   Your function should return true if any value appears at least twice in the array,
   and it should return false if every element is distinct.
 * */
class Solution {
public:
    // 思路：利用hashset检查
    bool containsDuplicate(vector<int>& nums) {
        if (nums.empty()) return false;
        unordered_set<int> dict;
        for (int i : nums){
            if (dict.count(i)) return true;
            dict.insert(i);
        }
        return false;
    }
};