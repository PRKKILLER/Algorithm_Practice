//
// Created by 薛智钧 on 2020/3/15.
//

#include <vector>
#include <iostream>
#include <unordered_map>  // same as hashmap
using namespace std;

/*Given an array of integers, return indices of the two numbers such that they add up to a specific target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * */

//  思路：因为题目说明只有一个解，因此可以便利一遍数组，元素存放在dict中。并将数组下标作为value,数组值作为keys
//  解题关键：运用哈希表
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dict;
        for (int i = 0; i < nums.size(); ++i) {
            if (dict.count(target - nums[i])) // 若dict中已存在target - nums[i]
                return {i, dict[target - nums[i]]};
            dict[nums[i]] = i;
        }
        return {};
    }
};

int main(){
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    Solution sol;
    vector<int> res = sol.twoSum(nums, 9);

    if (res.empty()) cout << "Null";
    for (int num:res)
        cout << num << " ";
}