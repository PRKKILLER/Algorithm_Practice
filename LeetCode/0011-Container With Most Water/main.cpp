//
// Created by 薛智钧 on 2020/4/7.
//
#include <vector>
#include <iostream>
using namespace std;


/*
 * Given n non-negative integers a1, a2, ..., an ,
 * where each represents a point at coordinate (i, ai).
 * n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
 * Find two lines, which together with x-axis forms a container,
 * such that the container contains the most water.
 * */
class Solution {
public:
    // 双指针算法：area = min (height[lo], height[hi]) * (hi - lo)
    // 若 minHeight = height[lo], 则应右移左指针，因为maxArea是被height[lo]所限制
    // 此时的area，已经是height[lo]所能得到的最大面积。
    // 若想增大面积，应右移左指针；同样的，若minHeight = height[hi],则应左移右指针
    int maxArea(vector<int>& height) {
        if (height.size() < 2) return 0;

        int lo = 0, hi = (int)height.size() - 1;
        int maxArea = 0;
        while (lo < hi){
            int minHeight = min(height[lo], height[hi]);
            int curArea = minHeight * (hi - lo);
            if (maxArea < curArea)
                maxArea = curArea;
            if (minHeight == height[lo])
                ++lo;
            else if (minHeight == height[hi])
                --hi;
        }
        return maxArea;
    }
};

int main(){
    vector<int> height = {1,8,6,2,5,4,8,3,1};
    Solution sol;
    cout << sol.maxArea(height);
}

