//
// Created by 薛智钧 on 2020/4/6.
//
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

// Given n non-negative integers representing an
// elevation map where the width of each bar is 1,
// compute how much water it is able to trap after raining.

// Example:
//
// Input: [0,1,0,2,1,0,1,3,2,1,2,1]
// Output: 6

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() < 2) return 0;

        stack<int> s;
        int water = 0, i = 0;
        while (i < height.size()){
            if (s.empty() || height[i] <= height[s.top()])
                s.push(i++);
            else{
                int pre = s.top(); s.pop();
                if (!s.empty()){
                    int minHeight = min(height[s.top()], height[i]);
                    water += (minHeight - height[pre]) * (i - s.top() - 1); // 长 * 宽
                }
            }
        }
        return water;
    }
};

int main(){
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    Solution sol;
    int water = sol.trap(height);
    cout << "The trapped water's amount is: "<< endl;
    cout << water;
}