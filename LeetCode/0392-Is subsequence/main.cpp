//
// Created by 薛智钧 on 2020/4/6.
//
#include <iostream>
#include <string>
using namespace std;

/*
 * Given a string s and a string t, check if s is subsequence of t.

  You may assume that there is only lower case English letters in both s and t.
  t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

 A subsequence of a string is a new string which is formed from
 the original string by deleting some (can be none) of the
 characters without disturbing the relative positions of the remaining characters.
 (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2
 * */

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        for (; i < s.size() && j < t.size(); ++j){
            if (s[i] == t[j]) ++i;
        }
        return i == s.size();
    }
};

int main(){
    string a = "";
    string b = "ahbadc";

    Solution sol;
    cout << sol.isSubsequence(a, b);
}

