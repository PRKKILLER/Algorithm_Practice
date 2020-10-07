//
// Created by 薛智钧 on 2020/4/6.
//
#include <iostream>
#include <vector>
#include <set>
using namespace std;


/*
 * Given two arrays, write a function to compute their intersection.

  Example:
  Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

  Note:

  Each element in the result must be unique.
  The result can be in any order.
 * */

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.empty() || nums2.empty()) return {};
        set<int> s1(nums1.begin(), nums1.end());
        set<int> s2(nums2.begin(), nums2.end());
        vector<int> res;
        for (auto i : s2){
            if (s1.count(i))
                res.push_back(i);
        }
        return res;
    }
};

int main(){
    vector<int> nums1 = {4,9,5};
    vector<int> nums2 = {9,4,9,8,4};
    Solution sol;
    vector<int> res = sol.intersection(nums1, nums2);
    for (int i : res){
        cout << i << " ";
    }
}