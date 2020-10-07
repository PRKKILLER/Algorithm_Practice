//
// Created by 薛智钧 on 2020/4/7.
//
#include <string>
#include <iostream>
using namespace std;

/*
 * Given a string s, find the longest palindromic substring in s.
 * You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
 * */

class Solution {
public:
    // 双指针从数组两侧搜索，时间复杂度O(n^2)
    string longestPalindrome(string s) {
        if (s.size() < 2) return s;
        string res = s.substr(0, 1); // substr(pos, n)
        int maxLen = 1;
        for (int i = 0; i < s.size(); ++i){
            int lo = i, hi = (int)s.size() - 1;
            int rStart = hi; // 暂存hi的起始位置
            int curLen = hi - lo + 1;
            while (lo <= hi){
                if (s[lo] == s[hi]){
                    ++lo; --hi;
                }else{ // s[lo] != s[hi]
                    lo = i; // 将lo指针复位
                    hi = --rStart; // 将hi复位
                    curLen = hi - lo + 1;
                }
            }
            if (curLen > maxLen){
                maxLen = curLen;
                res = s.substr(i, maxLen);
            }
        }
        return res;
    }

    // 思路：验证回文串的方式就是两个两个比较是否相等
    // 就要以一个数字为中心向两边expand，扩散寻找子串
    // 此时要考虑两种情况，字符串长度为奇数，eg. "bob"
    // 和字符串长度为偶数，eg. "noon"
    string longestPalindrome_2(string s){
        if (s.size() < 2) return s;
        int start = 0, maxLen = 1;
        for (int i = 0; i < s.size() - 1; ++i){
            // 假设回文串为长度为奇数
            expand(s, i, i, start, maxLen);
            // 假设回文串长度为偶数
            // 以两个数字为中心数
            expand(s, i, i + 1, start, maxLen);
        }
        return s.substr(start, maxLen);
    }

    static void expand(string& s, int lo, int hi, int& start, int& maxLen){
        // while循环退出时，s[lo]已经不等于s[hi]
        // 所以此时 curLen = hi - lo - 1
        // start = lo + 1
        while (0 <= lo && hi < s.size() && s.at(lo) == s.at(hi)){
            --lo; ++hi;
        }
        if (maxLen < hi - lo - 1){
            start = lo + 1;
            maxLen = hi - lo - 1;
        }
    }
};

int main(){
    string s = "aaabaaaa";
    Solution sol;
    cout << sol.longestPalindrome_2(s);
}

