//
// Created by 薛智钧 on 2020/4/8.
//
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
 * Given an array of size n, find the majority element.
 * The majority element is the element that appears more than ⌊ n/2 ⌋ times.

   You may assume that the array is non-empty
   and the majority element always exist in the array.

   Example 1:

   Input: [3,2,3]
   Output: 3
 * */

class Solution {
public:
    /*
     *  摩尔投票法 Moore Voting，需要 O(n) 的时间和 O(1) 的空间。
     *  这种投票法先将第一个数字假设为过半数，然后把计数器设为1，比较下一个数和此数是否相等，
     *  若相等则计数器加一，反之减一。然后看此时计数器的值，若为零，则将下一个值设为候选过半数。
     *  以此类推直到遍历完整个数组，当前候选过半数即为该数组的过半数。不仔细弄懂摩尔投票法的精髓的话，
     *  过一阵子还是会忘记的，首先要明确的是这个叼炸天的方法是有前提的，
     *  就是数组中一定要有过半数的存在才能使用，下面来看本算法的思路，这是一种先假设候选者，
     *  然后再进行验证的算法。现将数组中的第一个数假设为过半数，然后进行统计其出现的次数，
     *  如果遇到同样的数，则计数器自增1，否则计数器自减1，如果计数器减到了0，则更换下一个数字为候选者。
     *  这是一个很巧妙的设定，也是本算法的精髓所在，为啥遇到不同的要计数器减1呢，为啥减到0了又要更换候选者呢？
     *  首先是有那个强大的前提存在，一定会有一个出现超过半数的数字存在，那么如果计数器减到0了话，
     *  说明目前不是候选者数字的个数已经跟候选者的出现个数相同了，那么这个候选者已经很 weak，
     *  不一定能出现超过半数，此时选择更换当前的候选者。那有可能你会有疑问，
     *  那万一后面又大量的出现了之前的候选者怎么办，不需要担心，如果之前的候选者在后面大量出现的话，
     *  其又会重新变为候选者，直到最终验证成为正确的过半数
     * */

    static int majorityElement(vector<int>& nums){
        int res = 0, cnt = 0;
        for (int a : nums){
            if (cnt == 0) {
                res = a;
                ++cnt;
            }else{
                a == res ? ++cnt : --cnt;
            }
        }
        return res;
    }

    static int majorityElement_2(vector<int>& nums) {
        if (nums.size() < 2) return nums[0];

        sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        int i = 0, j = 1;
        for (; j < n; ++j){
            if (nums[i] != nums[j]){
                if (j - i > n / 2)
                    return nums[i];
                i = j;
            }
        }
        return nums[i];
    }
};

int main(){
    vector<int> vec = {3,3,3,2};
    cout << Solution::majorityElement(vec);
}

