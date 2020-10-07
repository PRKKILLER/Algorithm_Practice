//
// Created by 薛智钧 on 2020/5/20.
//
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
/*
 * 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，
 * 在子字符串中都恰好出现了偶数次。

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
 * */

class Solution {
public:
    static int findTheLongestSubstring(string s) {
        // state表示当前前缀串的状态
        int res = 0, state = 0, n = (int)s.size();
        // 状态数组用来存储每个状态对应的下标 pos[state] = index，替代hashmap
        vector<int> pos(32, -1);
        pos[0] = 0; // 初始状态为0
        for (int i = 0; i < n; ++i){
            switch (s[i]) {
                case 'a': state ^= (1 << 0); break;
                case 'e': state ^= (1 << 1); break;
                case 'i': state ^= (1 << 2); break;
                case 'o': state ^= (1 << 3); break;
                case 'u': state ^= (1 << 4); break;
            }
            if (pos[state] != -1) {
                res = max(res, i + 1 - pos[state]);
            } else {
                pos[state] = i + 1;
            }
        }
        return res;
    }

    static int findLongestSubstring(string s){
        int res = 0, state = 0, n = (int)s.size();
        unordered_map<int, int> m{{0, -1}}; // state: position
        for (int i = 0; i < n; ++i){
            switch(s[i]) {
                case 'a': state ^= (1 << 0); break;
                case 'e': state ^= (1 << 1); break;
                case 'i': state ^= (1 << 2); break;
                case 'o': state ^= (1 << 3); break;
                case 'u': state ^= (1 << 4); break;
            }
            if (!m.count(state)) m[state] = i;
            res = max(res, i - m[state]);
        }
        return res;
    }
};


int main() {
    string s = "abi";
    cout << Solution::findLongestSubstring(s);
}