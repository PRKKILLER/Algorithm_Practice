//
// Created by 薛智钧 on 2020/4/7.
//
#include <vector>
#include <iostream>
using namespace std;

/*
 * Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
 * Find all unique triplets in the array which gives the sum of zero.
 *
 * Example:

   Given array nums = [-1, 0, 1, 2, -1, -4],

   A solution set is:
   [
    [-1, 0, 1],
    [-1, -1, 2]
  ]
 * */

class Solution {
public:
    // 找到3个数，使其和=0。则应先fix一个数，让后两个数是该数字的相反数
    // 因此可以先对数组进行排序，然后遍历数组，若遇到正数就直接break
    // 因为当前数字若为正，则后续数均＞0，不可能存在和为0的情况
    // 同时，还要跳过重复的情况。因此从第二个数开始，要检查其与前一个数字是否相同，
    // 若相同，则跳过，因为不想同一个数字被fix两次
    vector<vector<int>> threeSum(vector<int>& nums) {
        heap_sort(nums, nums.size()); // 对数组进行排序
        if (nums.empty() || nums.front() > 0 || nums.back() < 0) return {};
        vector<vector<int>> res;
        for (int k = 0; k < (int)nums.size() - 2; ++k){ // 遍历到倒数第3个数停止
            if (nums[k] > 0) break;
            if (k > 0 && nums[k - 1] == nums[k]) continue; // 跳过重复数字情况
            int target = 0 - nums[k];
            int i = k + 1, j = (int)nums.size() - 1;
            while (i < j){
                if (nums[i] + nums[j] == target){
                    res.push_back({nums[k], nums[i], nums[j]});
                    while (i < j && nums[i] == nums[i + 1]) ++i;
                    while (i < j && nums[j] == nums[j - 1]) --j;
                    ++i; --j;
                }else if(nums[i] + nums[j] < target){
                    ++i;
                }else{
                    --j;
                }
            }
        }
        return res;
    }

    static void heap_sort(vector<int>& arr, int len){
        // 建大顶堆
        for (int i = len / 2 - 1; i >=0; --i){
            adjustHeap(arr, i, len);
        }

        for (int j = len - 1; j > 0; --j){
            swap(arr[0], arr[j]); // 交换堆顶和堆尾元素
            adjustHeap(arr, 0, j); // 重新构建大顶堆
        }
    };

    static void adjustHeap(vector<int>& arr, int i, int len){
        int tmp = arr[i];
        for (int k = 2 * i + 1; k < len; k = 2 * k + 1){ // 从当前节点的左孩子开始
            if (k + 1 < len && arr[k] < arr[k + 1]) ++k; // k指向右孩子
            if (tmp < arr[k]){ // 若父节点的值小于子节点，则将子节点的值赋予父节点
                arr[i] = arr[k];
                i = k;
            }
        }
        arr[i] = tmp; // tmp存放的最终位置
    }

    static void printArray(vector<vector<int>>& arr){
        for (const vector<int>& a : arr){
            for (auto i : a){
                cout << i << " ";
            }
            cout << endl;
        }
    }
};

int main(){
    vector<int> vec = {-1, 0, 1, 2, -1, -4};
    Solution sol;
    vector<vector<int>> res = sol.threeSum(vec);
    Solution::printArray(res);
}

