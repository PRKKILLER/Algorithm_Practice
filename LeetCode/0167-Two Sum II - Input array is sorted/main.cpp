//
// Created by 薛智钧 on 2020/3/23.
//
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
 * Given an array of integers that is already sorted in ascending order,
 * find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers
 such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and
you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
 * */

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int>loc;
        for (int i = 0; i < numbers.size(); ++i) {
            if (loc.count(target - numbers[i]))
                return {loc[target-numbers[i]] + 1, i + 1};
            else
                loc[numbers[i]] = i;
        }
        return {};
    }

    // 思路：利用2 pointer从头和尾扫描数组
    // 因为array是sorted的，因此起始时start指向array中的最小值，
    // last 指向array中的最大值
    vector<int> twoSum_2(vector<int>& numbers, int target){
        int first = 0, last = numbers.size() - 1;
        while (true){
            if (numbers[first] + numbers[last] < target)
                ++first;
            else if (numbers[first] + numbers[last] > target)
                --last;
            else
                return {first + 1, last + 1};
        }
    }

};

