//
// Created by 薛智钧 on 2020/5/27.
//
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
 *  Given an array A of integers, return the number of (contiguous, non-empty)
 *  subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Note:
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
 * */

class Solution {
public:
    // complexity = O(n^2) TLE
    static int subarraysDivByK(vector<int>& A, int K) {
        int res = 0;
        for (int i = 0; i < A.size(); ++i){
            auto tmp = 0;
            for (int j = i; j < A.size(); ++j){
                tmp += A[j];
                tmp % K == 0 ? ++res : res = res;
            }
        }
        return res;
    }

    // 利用 prefix Sum 和 hashmap进行计算
    static int subarraysDivByK_2(vector<int>& A, int K){
        // 初始化边界情况，预设preSum[-1] = 0
        // -1代表数组的-1项，即表示求数组第0项的前缀和之前，前缀和modK = 0已经出现过一次了
        // m: key = preSumModK value = preSumModK出现过的次数
        unordered_map<int, int> m{{0, 1}};
        auto preSumModK = 0; //保存前缀和模K的结果
        int cnt = 0; // 保存计数
        for (int a : A){
            preSumModK = (preSumModK + a) % K; // 前缀和模的递推公式
            if (preSumModK < 0) preSumModK +=K; // 处理除数为负的情况
            // 之前存在过与当前preSum相等的key，出现过几次 ，就可以与当前前缀和，差分出几个满足条件的子数组
            // 因此 cnt += m[preSumModK]
            if (m.count(preSumModK)){
                cnt += m[preSumModK];
            }
            ++m[preSumModK];
        }
        return cnt;
    }

    // 因为 preSum % k的值只会在[0, k-1]中取值，因此可以利用vector代替hashmap
    static int subarraysDivByK_3(vector<int>& A, int K) {
        vector<int> m(K); // 初始长度为k的数组，作为hashmap的替代
        m[0] = 1;
        int cnt = 0, preSumModK = 0;
        for (int a : A){
            preSumModK = (preSumModK + a) % K;
            if (preSumModK < 0) preSumModK += K;
            if (m[preSumModK]){
                cnt += m[preSumModK];
                ++m[preSumModK];
            } else {
                m[preSumModK] = 1;
            }
        }
        return cnt;
    }

    static int subarraysDivByK_4(vector<int>& A, int K){
        vector<int> mod_map(K);
        mod_map[0] = 1;
        int cnt = 0, preSum = 0, preSumModK = 0;
        for (int a : A) {
            preSum += a;
            preSumModK = preSum % K;
            if (preSumModK < 0) preSumModK += K;
            if (mod_map[preSumModK]){
                cnt += mod_map[preSumModK];
                ++mod_map[preSumModK];
            } else {
                mod_map[preSumModK] = 1;
            }
        }
        return cnt;
    }

};

int main(){
    vector<int> vec = {4,5,0,-2,-3,1};
//    cout << Solution::subarraysDivByK_3(vec, 5);
    cout << -3 % (6);
}