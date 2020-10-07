//
// Created by 薛智钧 on 2020/4/6.
//
#include <string>
#include <iostream>
using namespace std;

/* 题意是n=1时输出字符串1；
   n=2时，数上次字符串中的数值个数，因为上次字符串有1个1，所以输出11；
   n=3时，由于上次字符是11，有2个1，所以输出21；
   n=4时，由于上次字符串是21，有1个2和1个1，所以输出1211。
   n=5时, 输出：111221
   依次类推，写个countAndSay(n)函数返回字符串。
 */

class Solution {
public:
    string countAndSay(int n) {
        if (n < 1) return "";

        string res = "1";
        for (int k = 2; k <= n; ++k){
            string cur;
            for (int i = 0; i < res.size(); ++i){ // 遍历
                int cnt = 1;
                while (i + 1 < res.size() && res[i] == res[i+1]){
                    ++cnt;
                    ++i;
                }
                cur += to_string(cnt) + res[i];
            }
            res = cur;
        }
        return res;
    }
};

int main(){
    int c = 4;
    Solution sol;
    cout << sol.countAndSay(c);
}

