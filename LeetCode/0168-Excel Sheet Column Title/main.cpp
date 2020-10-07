//
// Created by 薛智钧 on 2020/3/31.
//
#include <string>
#include <iostream>
using namespace std;

/*
 * Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
   701 ->ZY
 * */

class Solution {
public:
    // 从低位往高位求，每进一位，则把原数缩小26倍，再对26取余，之后减去余数
    // 对于小于26的数字，只需要对26取余，然后减去1，加上字符A即可
    string convertToTitle(int n) {
        if (n < 1) return "";
        string res;
        while (n){
            int mod = (n - 1) % 26; // 因为要与'A'相加，因此要先－1再取余
            res += (char)(mod + 'A'); // 'Z' = 'A' + 25
            n -= (mod + 1); // 减去真正的余数
            n /= 26;
        }
        reverse(res.begin(), res.end());
        return res;
    }

    // 递归法
    string convertToTitle_R(int n){
        return n == 0 ? "" :
        convertToTitle_R((n - 1) / 26) + (char)((n - 1) % 26 + 'A');
    }
};

int main(){
    int n = 99;
    Solution sol;
    cout << sol.convertToTitle(n);
}