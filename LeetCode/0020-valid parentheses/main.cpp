//
// Created by 薛智钧 on 2020/3/16.
//
#include <iostream>
#include <string>
#include <stack>
using namespace std;

/*
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
 */

// 思路利用stack判断括号是否成对
class Solution {
public:
    bool isValid(string s) {
        if (s.empty()) return true; // 空字符串是valid
        string left = "([{", right = ")]}";
        stack<char> check;
        for (char c:s){
            if (left.find(c) != string::npos)
                check.push(c); // 是左括号则入栈
            else{ // 当前符号属于 right
                if (check.empty()) return false;
                int r_index = right.find(c);
                int l_index = left.find(check.top());
                if (r_index != l_index) return false; // 若栈顶括号和当前括号不匹配
                check.pop();
            }
        }
        return check.empty();
    }
};

int main(){
    string s = "([])";
    Solution sol;
    cout << sol.isValid(s);
}
