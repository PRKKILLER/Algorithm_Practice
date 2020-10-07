//
// Created by 薛智钧 on 2020/3/17.
//

/*
 * You are a product manager and currently leading a team to develop a new product.
 * Unfortunately, the latest version of your product fails the quality check.
 * Since each version is developed based on the previous version,
 * all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version.
You should minimize the number of calls to the API.
 * */


// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
    // 搜索题优先考虑二分查找
    // 因为好坏版本之间有一个分界点，因此可以用二分查找找到这个边界
public:
    int firstBadVersion(int n) {
        int lo = 0, hi = n;
        while (lo < hi){
            int mi = lo + (hi - lo) / 2; //不会越界
            isBadVersion(mi + 1) ? hi = mi : lo = mi +1;
        }
        return lo + 1; // 产品的version = 数组下表 + 1
    }
};

