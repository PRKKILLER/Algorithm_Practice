//
// Created by 薛智钧 on 2020/3/31.
//
#include <vector>
#include <list>
#include <iostream>
using namespace std;

/*
 * Given two sorted integer arrays nums1 and nums2,
 * merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2.

 * */
class Solution {
public:
    // 方法1: 利用list
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        list<int> res;
        int i = 0, j = 0; // 两个数组的指针
        while (i < m && j < n){
            if (nums1[i] < nums2[j])
                res.push_back(nums1[i++]);
            else
                res.push_back(nums2[j++]);
        }
        if (i < m)
            while (i < m) res.push_back(nums1[i++]);
        else if (j < n)
            while (j < n) res.push_back(nums2[j++]);

        i = 0; auto iter = res.begin();
        for(; iter != res.end(); ++i, ++iter)
            nums1[i] = *iter;
    }

    // 方法2：逆向指针，不需要额外空间
    // 因为
    void merge_2(vector<int>& nums1, int m, vector<int>& nums2, int n){
        if (nums1.empty() || nums2.empty()) return;

        int p1 = m - 1, p2 = n - 1, idx = m + n - 1;
        while (p1 >= 0 && p2 >= 0){
            if (nums1[p1] > nums2[p2])
                nums1[idx--] = nums1[p1--];
            else
                nums1[idx--] = nums2[p2--];
        }
        if (p2 >= 0)
            while (p2 >= 0) nums1[idx--] = nums2[p2--];
    }
};

int main(){
    vector<int> n1 = {0};
    vector<int> n2 = {1};
    Solution sol;
    sol.merge_2(n1, 0, n2, 1);
    for (int c : n1) cout << c << " ";
}