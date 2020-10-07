//
// Created by 薛智钧 on 2020/3/31.
//
#include <string>
#include <iostream>
#include <math.h>
using namespace std;

/*
 * Given a column title as appear in an Excel sheet, return its corresponding column number.

   For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
*/

class Solution {
public:
    // 从低位到高位
    int titleToNumber(string s) {
        if (s.empty()) return 0;
        int res = 0;
        auto iter = s.rbegin();
        for (int i = 0; i < s.size(); ++i, ++iter){
            int digit = *iter - 'A' + 1;
            res += (int)(digit * pow(26, i));
        }
        return res;
    }

    // 从高位到低位
    int titleToNumber_2(string s){
        int res = 0;
        for (char i : s)
            res = res * 26 + (i - 'A' + 1);
        return res;
    }
};

int main(){
    string s = "CU";
    Solution sol;
    cout << sol.titleToNumber_2(s);
}
