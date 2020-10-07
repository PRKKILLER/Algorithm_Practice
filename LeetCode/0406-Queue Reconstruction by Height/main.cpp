//
// Created by 薛智钧 on 2020/6/7.
//
#include <iostream>
#include <vector>
using namespace std;

/*
 *  Suppose you have a random list of people standing in a queue.
 *  Each person is described by a pair of integers (h, k),
 *  where h is the height of the person and
 *  k is the number of people in front of this person who have a height greater than or equal to h.
 *  Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
 * */

class Solution {
public:
    /*
     *  因为题目中的 k 只计算在他前面height不低于他的人的个数，因此在当前person前面比他矮的人的人数对k完全没有影响
     *  思路：首先根据height对数组进行排序，对于height相同的两个元素，将k值较小的排在前面。
        之后，新建一个空的数组，从前往后遍历数组，因为每次得到的[height, k]pair都是剩下pairs中最大的，
        因此就按照 pair 的 k 值插入到新的数组中去
     * */
    /*
     *  input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        subarray after step 1: [[7,0], [7,1]]
        subarray after step 2: [[7,0], [6,1], [7,1]]
        ...
     * */
    static vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](vector<int>& p1, vector<int>& p2) {
            return p1[0] > p2[0] || (p1[0] == p2[0] && p1[1] < p2[1]);
        });
        vector<vector<int>> res;
        for (auto pair : people)
            res.insert(res.begin() + pair[1], pair);
        return res;
    }
};

int main() {
    vector<vector<int>> people{{7,0},{4,4},{7,1},{5,0},{6,1},{5,2}};
    vector<vector<int>> res = Solution::reconstructQueue(people);
    for (auto pair : res) {
        cout << "[" << pair[0] <<"," << pair[1] <<"]" << " ";
    }
}
