//
// Created by 薛智钧 on 2020/5/23.
//
#include <vector>
#include <iostream>
using namespace std;

/*
 * 给定两个由一些闭区间组成的列表，每个区间列表都是成对不相交的，并且已经排序。

返回这两个区间列表的交集。

（形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。
 两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）

输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
注意：输入和所需的输出都是区间对象组成的列表，而不是数组或列表。
 
提示：

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
 * */

class Solution {
public:
    static vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>> res;
        for (auto i = 0, j = 0; i < A.size() && j < B.size(); ){
            if (A[i][1] < B[j][0]) ++i;
            else if (B[j][1] < A[i][0]) ++j;
            else {
                res.push_back({max(A[i][0], B[j][0]), min(A[i][1], B[j][1])});
                if (A[i][1] < B[j][1]) ++i;
                else ++j;
            }
        }
        return res;
    }

    static vector<vector<int>> intervalIntersection_2(vector<vector<int>>& A, vector<vector<int>>& B){
        vector<vector<int>> res;
        for (auto i = 0, j = 0; i < A.size() && j < B.size(); A[i][1] < B[j][1] ? ++i : ++j){
            auto start = max(A[i][0], B[j][0]);
            auto end = min(A[i][1], B[j][1]);
            if (start <= end)
                res.push_back({start, end});
        }
        return res;
    }
};

int main(){
    vector<vector<int>> A({{0,2}, {5,10}, {13, 23}, {24,25}});
    vector<vector<int>> B({{1,2}, {5,5}, {8, 10}, {15, 23}, {24,24},{25,25}});

    vector<vector<int>> res = Solution::intervalIntersection_2(A, B);
    for (auto item : res)
        cout << "[" << item[0] << "," << item[1] << "]" << " ";
}
