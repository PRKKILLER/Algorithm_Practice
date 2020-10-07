//
// Created by 薛智钧 on 2020/4/4.
//
#include <iostream>
#include <string>
using namespace std;

static inline void _do_reverse(char* str, const int len){
    char* beg = str;
    char* end = str + len - 1;
    for (; beg < end; ++beg, --end){
        char tmp = *beg;
        *beg = *end;
        *end = tmp;
    }
}

int string_reverse(char* str, const char token){
    if (!str || token == '\0') return -1;
    int beg = 0, end = 0; // 记录字符串中sub_string的起始位置
    for (; *(str + end); ++end){
        if (str[end] == token){
            _do_reverse(str + beg, end - beg);
            beg = end + 1;
        }
    }
    _do_reverse(str + beg, end - beg); // reverse最后一个字符串
    _do_reverse(str, end); // 全字符串反转
    return 0;
}

int main(){
    char test_str[][64] = {"www.baidu.com", "www.hust.edu.en"};
    for (int i = 0; i < sizeof(test_str) / sizeof(test_str[0]); ++i){
        cout << test_str[i] << "->";
        string_reverse(test_str[i], '.');
        cout << test_str[i] << endl;
    }
}