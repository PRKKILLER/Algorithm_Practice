//
// Created by 薛智钧 on 2020/3/16.
//

// Determine whether an integer is a palindrome.
// An integer is a palindrome when it reads the same backward as forward.
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;
class Solution {
public:

    // 利用string
    bool isPalindrome(int x) {
        string strNum = to_string(x);
        auto i = strNum.begin(), j = strNum.end() - 1;
        while (i != j){
            if (*i != *j) return false;
            if (i + 1 == j) return true;
            ++i; --j;
        }
        return true;
    }

    // 不利用string
    // 首先获得x的位数，然后依次比较最高位和最低位
    bool isPalindrome_2(int x){
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        int div = 1;
        while (x / div >= 10) div *= 10;  // div存储x的位数
        while (x > 0){
            int lo = x % 10;
            int hi = x / div;
            if (lo != hi) return false;
            // x%div 可将数字最高位舍去
            // (x%div) / 10 可将数字最低位舍去
            x = (x % div) / 10; // 去除数字的最高两位
            div /= 100;
        }
        return true;
    }
};

int main(){
    int num = 11;
    Solution sol;
    cout<<sol.isPalindrome_2(num);
}
