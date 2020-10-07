//
// Created by 薛智钧 on 2020/4/8.
//
#include <iostream>
using namespace std;

/*
 * Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
 The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
 so the second smallest number is 10.
 * */

class Solution {
public:
     static int findKthNumber(int n, int k) {
        int cur = 1;
        --k;
        while (k > 0) {
            long long step = 0, n1 = cur, n2 = cur + 1;
            while (n1 <= n) {
                step += min((long long)n + 1, n2) - n1;
                n1 *= 10;
                n2 *= 10;
            }
            if (step <= k) {
                ++cur;
                k -= step;
            } else {
                cur *= 10;
                --k;
            }
        }
        return cur;
    }
};

int main(){
    int n = 13, k = 2;
    int res = Solution::findKthNumber(n, k);
    cout << res;
}
