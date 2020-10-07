//
// Created by 薛智钧 on 2020/3/31.
//
#include <string>
#include <unordered_map>
#include <iostream>
using namespace std;

/**
 * Given a string S and a string T,
 * find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be
only one unique minimum window in S.
 * **/

class Solution {
public:
    // 利用滑动窗口法，利用左右指针控制窗口大小
    string minWindow(string s, string t) {
        int start = 0, minLen = INT_MAX; // 记录最短子串的开始位置和最短长度
        int left = 0, right = 0;
        unordered_map<char, int> dict;
        unordered_map<char, int> window;

        for (char c : t) ++dict[c]; // 保存目标子串的每个字符出现次数，方便后续查找
        int match = 0; // 当前子串匹配的字符个数

        while (right < s.size()){
            char c1 = s[right++]; // right指向下一个字符，此时window_size = right - left
            if (dict.count(c1)){
                ++window[c1];
                if (window[c1] == dict[c1])
                    ++match;
            }

            // 当前子串已满足条件，现在开始右移左指针，缩小window
            // dict的size和t不一定相同，
            // eg. t = "aa" size(t) = 2; size(dict) = 1
            while (match == dict.size()){
                if (right - left < minLen){
                    start = left; // 更新子串起始位置
                    minLen = right - left; // 更新最短长度
                }
                char c2 = s[left];
                if (dict.count(c2)){
                    --window[c2];
                    if (window[c2] < dict[c2])
                        --match;
                }
                ++left;
            }
        }
        return minLen == INT_MAX ? "" : s.substr(start, minLen);
    }
};

int main(){
    string s = "aa", t = "aa";
    Solution sol;
    string res = sol.minWindow(s, t);
    cout << res;
}

