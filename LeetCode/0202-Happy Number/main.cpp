//
// Created by 薛智钧 on 2020/3/22.
//

// Write an algorithm to determine if a number is "happy".
//
// A happy number is a number defined by the following process:
// Starting with any positive integer,
// replace the number by the sum of the squares of its digits,
// and repeat the process until the number equals 1 (where it will stay),
// or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy numbers.
#include <unordered_set>
using namespace std;


class Solution {
public:
    // 不是快乐数的情况：在循环过程中回到原本的数字，且过程中不包含 = 1 的 情况
    // 就不是快乐数

    // 思路： 用 HashSet 来记录所有出现过的数字，然后每出现一个新数字，
    // 在 HashSet 中查找看是否存在，若不存在则加入表中，若存在则跳出循环，
    // 并且判断此数是否为1，若为1返回true，不为1返回false
    bool isHappy(int n) {
        unordered_set<int> dict;  // hashset
        while (n != 1){
            int sum = 0;
            while (n){
                sum += (n % 10) * (n % 10); // 各位之和
                n /= 10;
            }
            n = sum;
            if (dict.count(n)) break;
            dict.insert(n);
        }
        return n == 1;
    }

    // 思路2：类似Linked List Cycle 快慢指针，检测是否成环
    // 区别在于这道题的环一定存在，但只有 slow == 1时是happy number
    // 其中慢指针每次进行1次迭代，快指针每次两次迭代
    // 若是happy number,则快指针会停在1上，与慢指针相遇
    // 若不是happy number，则会在非1上相遇

    bool isHappy_2(int n){
        int slow = n, fast = n;
        while (true){ // 一直循环，直到相遇
            slow = nextNum(slow);
            fast = nextNum(fast);
            fast = nextNum(fast);
            if (slow == fast)
                break;
        }
        return slow == 1;
    }

    static int nextNum(int n){
        int sum = 0;
        while (n){
            sum += (n % 10) * (n % 10);
            n /= 10;
        }
        return sum;
    }
};
