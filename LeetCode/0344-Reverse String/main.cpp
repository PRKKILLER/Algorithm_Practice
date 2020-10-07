//
// Created by 薛智钧 on 2020/4/3.
//

#include <string>
#include<vector>
#include<iostream>
using namespace std;

class Solution{
public:
    void reverseString(vector<char>& s){
        int len = s.size();
        if (len < 2) return;
        for (int i = 0; i < len / 2; ++i){
            char tmp = s[i];
            s[i] = s[len - 1 -i];
            s[len - 1 - i] = tmp;
        }
    }

    string reverseString2(string s){
        if (s.size() < 2) return s;
        return reverseString2(s.substr(1)) + s.at(0); // 每次将字符串的第一个数字取出放在末尾
    }
};

