//
// Created by 薛智钧 on 2020/3/22.
//

#include <iostream>
#include <vector>
using namespace std;

/*
 * Given an array, rotate the array to the right by k steps, where k is non-negative.

   Example 1:

  Input: [1,2,3,4,5,6,7] and k = 3
  Output: [5,6,7,1,2,3,4]
  Explanation:
  rotate 1 steps to the right: [7,1,2,3,4,5,6]
  rotate 2 steps to the right: [6,7,1,2,3,4,5]
  rotate 3 steps to the right: [5,6,7,1,2,3,4]
* */

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size(); // 归一化k
        if (k == 0) return;
        size_t last = nums.size() - k;
        vector<int> temp(nums.begin(), nums.begin() + last);
        copy(nums.begin() + last, nums.end(), nums.begin());
        copy(temp.begin(), temp.end(), nums.begin() + k);
    }

    // 利用映射: i -> (i + k) % n
    void rotate_2(vector<int>& nums, int k){
        vector<int> tmp = nums;
        size_t len = nums.size();
        for (int i = 0; i < len; ++i){
            nums[(i + k) % len] = tmp[i];
        }
    }

    // 思路：较为难以理解，建议画图理解
    // 每次交换可以使一个元素就位，时间复杂度为O(n)
    void rotate_3(vector<int>& nums, int k){
        if (nums.empty()) return;
        size_t len = nums.size();
        int start = 0; // 记录当前需要转换的部分的起始位置
        for (; k %= len; len -= k,start += k){
            for (int i = 0; i < k; ++i){
                swap(nums[start + i], nums[len - k + start + i]);
            }
        }
    }
};


int main(){
    vector<int> vec = {1,2};
    Solution sol;
    sol.rotate(vec, 1);
    for (int num : vec){
        cout << num << ",";
    }
}
