//
// Created by 薛智钧 on 2020/6/5.
//
#include <iostream>
#include <vector>
using namespace std;

/*
 * Given a matrix of m x n elements (m rows, n columns),
 * return all elements of the matrix in spiral order.
 *  Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 * */

class Solution {
public:
    static vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};
        vector<int> res;
        int r_start = 0, r_end = matrix.size() - 1; // row_start, row_end
        int c_start = 0, c_end = matrix[0].size() - 1; // column_start, column_end
        while (r_start <= r_end && c_start <= c_end) {
            // 处理只有一列的情况，不然会重复计算
            if (c_start == c_end) {
                for (int i = r_start; i <= r_end; ++i)
                    res.push_back(matrix[i][c_start]);
                return res;
            }
            // 处理只有一行的情况，不然会重复计算
            if (r_start == r_end) {
                for (int j = c_start; j <= c_end; ++j)
                    res.push_back(matrix[r_start][j]);
                return res;
            }
            for (int j = c_start; j <= c_end; ++j) // traverse right
                res.push_back(matrix[r_start][j]);
            for (int i = r_start + 1; i <= r_end; ++i) // traverse down
                res.push_back(matrix[i][c_end]);
            for (int j = c_end - 1; j >= c_start; --j) // traverse left
                res.push_back(matrix[r_end][j]);
            for (int i = r_end - 1; i >= r_start + 1; --i) // traverse up
                res.push_back(matrix[i][c_start]);
            ++r_start, --r_end;
            ++c_start, --c_end;
        }
        return res;
    }
};

int main() {
    vector<vector<int>> matrix{{1,2,3}};
    vector<int> res = Solution::spiralOrder(matrix);
    for (int a : res)
        cout << a << " ";
}
