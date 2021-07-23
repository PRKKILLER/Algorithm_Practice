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
    int start_row = 0, end_row = matrix.size() - 1;
    int start_col = 0, end_col = matrix[0].size() - 1;
    int dir = 0;
    vector<int> res;

    while (start_row <= end_row && start_col <= end_col) {
      switch (dir) {
        case 0:  // right direction
          for (int c = start_col; c <= end_col; ++c) {
            res.push_back(matrix[start_row][c]);
          }
          ++start_row;
          break;
        case 1:  // down direction
          for (int r = start_row; r <= end_row; ++r) {
            res.push_back(matrix[r][end_col]);
          }
          --end_col;
          break;
        case 2:  // left direction
          for (int c = end_col; c >= start_col; --c) {
            res.push_back(matrix[end_row][c]);
          }
          --end_row;
          break;
        case 3:  // up direction
          for (int r = end_row; r >= start_row; --r) {
            res.push_back(matrix[r][start_col]);
          }
          ++start_col;
          break;
      }
      dir = (dir + 1) % 4;
    }

    return res;
  }
};

int main() {
  vector<vector<int>> matrix{{1, 2, 3}};
  vector<int> res = Solution::spiralOrder(matrix);
  for (int a : res) cout << a << " ";
}
