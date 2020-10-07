//
// Created by 薛智钧 on 2020/3/16.
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".*/


// 思路: 以字符串数组的第一个字符串为基准，寻找最长字符串
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string maxPrefix;

        int index = 0;
        for (char c : strs[0]){ // 遍历strs[0]的每个元素
            for (int i = 1; i < strs.size(); ++i){
                if (strs[i].size() <= index || c != strs[i].at(index))
                    return maxPrefix;
            }
            maxPrefix += c; // 将当前字符连接到maxPrefix
            ++index;
        }
        return maxPrefix;
    }
};

int main(){
    vector<string> strs;
    strs.push_back("111");
    strs.push_back("12");
    Solution sol;
    cout << "the longest common prefix is: "
         << sol.longestCommonPrefix(strs);
}
