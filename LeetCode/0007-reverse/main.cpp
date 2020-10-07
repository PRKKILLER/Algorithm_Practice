//
// Created by 薛智钧 on 2020/3/16.
//

// Given a 32-bit signed integer, reverse digits of an integer. (越界返回0)
// Assume we are dealing with an environment
// which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
// For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#include <iostream>
#include <climits>

class Solution {
public:

    // 在每步逆序时检查数字是否越界
    // INT_MAX = 2^31 - 1
    // INT_MIN = -2^31
    int reverse(int x) {
        int res = 0;
        while (x){
            int temp  = x % 10; // 取得个位数
            x /= 10;
            // 越界检查 注: int 最大值和最小值不对称
            // 负数的余数也是负数
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && temp > 7))
                return 0;
            if (res < INT_MIN /10 || (res == INT_MIN / 10 && temp < -8))
                return 0;

            res = res * 10 + temp;
        }
        return res;
    }
};
