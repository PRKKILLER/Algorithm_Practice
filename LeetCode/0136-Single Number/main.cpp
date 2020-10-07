//
// Created by 薛智钧 on 2020/3/23.
//
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;


class Solution {
    // Given a non-empty array of integers,
    // every element appears twice except for one. Find that single one.
    //
    // Note:
    // Your algorithm should have a linear runtime complexity.
    // Could you implement it without using extra memory?
public:
    // 思路1: 利用hashmap
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> dict;
        for (int num : nums){
            dict[num] += 1;
        }
        for (int num : nums){
            if (dict[num] == 1)
                return num;
        }
    }
    // 利用除了target，每个数字都会出现2次的特点
    // 思路: 利用数学: 2 * (a+b+c) - (a+a+b+b+c) = c
    int singleNumber_2(vector<int>& nums){
        int setSum = 0, numSum = 0;
        unordered_set<int> dict;
        for (int num : nums){
            if (!dict.count(num)){
                dict.insert(num);
                setSum += num;
            }
            numSum += num;
        }
        return 2 * setSum - numSum;
    }

    // 思路3: 利用异或运算
    // a (xor) 0 = a; a (xor) a = 0;
    // a (xor) b (xor) a = (a(xor)a)(xor)b = 0 (xor) b = b

    int singleNumber_3(vector<int>& nums){
        int res = 0;
        for (int num : nums){
            res ^= num;
        }
        return res;
    }
};
