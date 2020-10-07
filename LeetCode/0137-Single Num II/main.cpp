//
// Created by 薛智钧 on 2020/3/23.
//

#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

/*
 * Given a non-empty array of integers,
 * every element appears three times except for one,
 * which appears exactly once. Find that single one.

 Note:
 Your algorithm should have a linear runtime complexity.
 Could you implement it without using extra memory?
 * */

class Solution {
public:
    // 利用hashset
    // res = (3*setSum - numSum) / 2
    int singleNumber(vector<int>& nums) {
        long setSum = 0, numSum = 0; // 若用int，可能越界
        unordered_set<int> dict;
        for (int num : nums){
            if (!dict.count(num)){
                dict.insert(num);
                setSum += num;
            }
            numSum += num;
        }
        return (int)((3 * setSum - numSum) / 2);
    }
};

