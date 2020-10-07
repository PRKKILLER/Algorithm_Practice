//
// Created by 薛智钧 on 2020/6/6.
//
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
 *  Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
 * */

class Solution {
public:
    /*
     *  因为时间复杂度为O(n)，因此不能对数组进行排序，考虑用hashmap
     *  关键点在于不断tracking sequence的长度，并且对当前连续sequence的头尾两个节点进行update
     *  也就是说，对于一个连续sequence {1,2,3,4}，map.get(1)和map.get(4)都应该返回4
     *  当将一个新的num加入到map中，首先检查(num-1)和(num+1)是否存在，若存在
     *  则加入num之后的连续sequence长度为map.get(num-1)+map.get(num+1)+1
     *  然后更新boundary的长度：map.get(num-left) = map.get(num+right)=newLength
     * */
    static int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> seq_map;
        int maxLen = 0;
        for (int num : nums) {
            // 注：不能用map.count(num)判断当前map中是否已存在num，
            // 因为即使map中原来不存在element,
            // 在使用map[element]之后，map[element]会被赋值为default value = 0
            if (seq_map[num]) continue; // map中已存在相同的num，跳过
            else {
                int left_len = seq_map[num - 1]; // 左侧seq若不存在，返回0
                int right_len = seq_map[num + 1]; // 右侧seq若不存在，返回0
                int newLen = left_len + right_len + 1;
                maxLen = max(newLen, maxLen);
                // 更新boundary的长度，忽略boundary之间的数值，只更新boundary
                if (left_len) seq_map[num - left_len] = newLen;
                if (right_len) seq_map[num + right_len] = newLen;
                // 在map中保存每个新数字，防止重复
                seq_map[num] = newLen;
            }
        }
        return maxLen;
    }
};

int main() {
    vector<int> nums = {1,7,5,4,3,2};
    cout << Solution::longestConsecutive(nums);
}

