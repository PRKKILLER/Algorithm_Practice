//
// Created by 薛智钧 on 2020/3/16.
//
#include <string>
#include <iostream>
#include <unordered_map>
using namespace std;

// Given a string, find the length of the longest substring without repeating characters.
/*
 * Input: "abcabcbb"
   Output: 3
   Explanation: The answer is "abc", with the length of 3.
 * */
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLen = 0, n = s.size();
        unordered_map<char, int> dict;
        for (int i = 0; i < n; ++i){
            dict.clear();
            int currLen = 0;
            if (n - i <= maxLen) break;
            for (int j = i; j < s.size(); ++j){
                if (dict.count(s[j]) == 0){
                    dict[s[j]] = 1;
                    ++currLen;
                    maxLen = max(currLen, maxLen);
            } else
                break;
            }
        }
        return maxLen;
    }

    // 利用sliding_window的思路解题
    // 找到最长子串的本质是维护一个滑动窗口，在元素不重复的条件下向右不断拓展
    // 当遇到相同的字符，就改变滑动窗口的左侧指针位置
    int lengthOfLongestSubstring_2(string s){
        int maxLen = 0, left = -1; // left 是无重复子串最左端的前一个位置
        int n = s.size();
        unordered_map<char, int>dict;
        for(int i = 0; i < n; ++i){
            if (dict.count(s[i]) && dict[s[i]] > left)
                left = dict[s[i]];
            dict[s[i]] = i;
            maxLen = max(i - left, maxLen);
        }
        return maxLen;
    }

    // 利用左右指针法 (也可以看作是滑动窗口法)
    int lengthOfLongestSubstring_3(string s){
        int left = 0, right = 0;
        int maxLen = 0;
        unordered_map<char, int> window;
        while (right < s.size()){
            char c1 = s[right];
            ++window[c1]; // 对当前字符计数
            ++right; // 当前滑动窗口的右侧，也即当前遍历的字符数
            while (window[c1] > 1){ // 出现重复字符，移动left指针，直至消除重复字符
                char c2 = s[left];
                --window[c2];
                ++left;
            }
            maxLen = max(maxLen, right - left);
        }
        return maxLen;
    }
};


int main(){
    string s = "abba";
    Solution sol;
    cout << sol.lengthOfLongestSubstring_2(s);
}

