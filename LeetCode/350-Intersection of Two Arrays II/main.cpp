//
// Created by 薛智钧 on 2020/4/6.
//
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

/*
 * Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
 * */

/*Follow up:
 * What if elements of nums2 are stored on disk,
 * and the memory is limited such that you cannot load all elements into the memory at once?
 *
 * 1. If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap,
 * read chunks of array that fit into the memory, and record the intersections.

   2. If both nums1 and nums2 are so huge that neither fit into the memory,
   sort them individually (external sort),
   then read 2 elements from each array at a time in memory, record intersections.
 * */

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.empty() || nums2.empty()) return {};

        mySort(nums1, 0, nums1.size());
        mySort(nums2, 0, nums2.size());
        vector<int>res;
        for (auto i = nums1.begin(), j = nums2.begin(); i != nums1.end() && j != nums2.end();){
            if (*i < *j) ++i;
            else if (*j < *i) ++j;
            else{
                res.push_back(*i);
                ++i; ++j;
            }
        }
        return res;
    }

    static int partition(vector<int>& arr, int lo, int hi){
        random_shuffle(arr.begin() + lo, arr.begin() + hi);
        int pivot = arr[lo]; --hi;
        while (lo < hi){
            while (lo < hi && pivot <= arr[hi]) --hi;
            if (lo < hi) arr[lo++] = arr[hi];
            while(lo < hi && arr[lo] <= pivot) ++lo;
            if (lo < hi) arr[hi--] = arr[lo];
        }
        arr[lo] = pivot;
        return lo;
    }

    static void mySort(vector<int>& arr, int lo, int hi){
        if (hi - lo < 2) return;

        int mi = partition(arr, lo, hi);
        mySort(arr, lo, mi);
        mySort(arr, mi + 1, hi);
    }
};

class Solution2{
public:
    // 用 HashMap 来建立 nums1 中字符和其出现个数之间的映射,
    // 然后遍历 nums2 数组，如果当前字符在 HashMap 中的个数大于0，
    // 则将此字符加入结果 res 中，然后 HashMap 的对应值自减1，参见代码如下：
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2){
        if (nums1.empty() || nums2.empty()) return {};

        vector<int> res;
        unordered_map<int, int> dict;
        for (auto i : nums1) ++dict[i];
        for (auto i : nums2){
            if (dict[i]-- > 0) res.push_back(i);
        }
        return res;
    }
};

int main(){
    vector<int> nums1 = {4,9,5};
    vector<int> nums2 = {9,4,9,8,4};
    Solution2 sol;
    vector<int> res = sol.intersect(nums1, nums2);
    for (int i : res){
        cout << i << " ";
    }
}



