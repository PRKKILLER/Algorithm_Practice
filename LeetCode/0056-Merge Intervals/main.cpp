//
// Created by 薛智钧 on 2020/5/23.
//
#include <vector>
#include <iostream>
using namespace std;

/*
 *  Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

注意：intervals数组并不是有序的，因此需要先排序
 * */

class Solution {
private:
    static bool cmp(const vector<int>& a, const vector<int>& b){
        return a[0] < b[0];
    }
public:
    static vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.size() < 2) return intervals;

        sort(intervals.begin(), intervals.end(), cmp);
        vector<vector<int>> res;
        for (int i = 0; i < intervals.size(); ){
            vector<int> tmp = intervals[i];
            int j = i + 1;
            for (; j < intervals.size() && intervals[j][0] <= tmp[1]; ++j){
                tmp[1] = max(intervals[j][1], tmp[1]);
            }
            res.push_back(tmp);
            i = j;
        }
        return res;
    }

    static vector<vector<int>> merge_2(vector<vector<int>>& intervals){
        if (intervals.size() < 2) return intervals;

        sort(intervals.begin(), intervals.end(), cmp);
        vector<vector<int>> res({intervals[0]});
        for (auto item : intervals){
            if (item[0] <= res.back()[1])  // overlapping intervals
                res.back()[1] = max(item[1], res.back()[1]);
            else
                res.push_back(item);
        }
        return res;
    }
};

int main(){
    vector<vector<int>> intervals({{1,6}, {3, 5}, {4, 7}});
    vector<vector<int>> test({{1,4}, {0,5}});
    vector<vector<int>> res = Solution::merge_2(test);
    for (auto item : res)
        cout << "[" << item[0] << "," << item[1] << "]" << " ";
}

