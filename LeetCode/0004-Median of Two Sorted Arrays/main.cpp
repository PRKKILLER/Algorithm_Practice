//
// Created by 薛智钧 on 2020/5/24.
//
#include <iostream>
#include <vector>
using namespace std;

/*
 *  There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
 * */

class Solution {
public:
    // time complexity: O(m+n)
    static double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merge;
        auto i = 0, j = 0;
        double res;
        for (; i < nums1.size() && j < nums2.size(); )
            nums1[i] < nums2[j] ? merge.push_back(nums1[i++]) : merge.push_back(nums2[j++]);

        while (i < nums1.size()) merge.push_back(nums1[i++]);
        while (j < nums2.size()) merge.push_back(nums2[j++]);

        auto n = merge.size();
        n % 2 == 0 ? res = ((merge[n / 2 - 1] + merge[n / 2])) / (double)2 : res = (double)merge[n / 2];
        return res;
    }

    // time complexity: O(log(min(m, n))
    static double findMedianSortedArrays_2(vector<int>& nums1, vector<int>& nums2) {
        // if nums1.size() is greater than nums2.size(), switch, to insure nums1.size <= nums2.size()
        if (nums1.size() > nums2.size())
            return findMedianSortedArrays_2(nums2, nums1);

        // when shorter array is empty
        if (nums1.empty()) {
            auto n = nums2.size();
            if (n % 2 == 0)
                return (((nums2[n / 2 - 1] + nums2[n / 2])) / (double)2);
            else
                return (double)nums2[n / 2];
        }

        int x = nums1.size(), y = nums2.size();
        int lo = 0, hi = x;
        // do the binary search on nums1
        while (lo <= hi) {
            int partitionX = (lo + hi) / 2;
            int partitionY = (x + y + 1) / 2 - partitionX;

            // if partitionX == 0, that means nothing is there on the left side,
            // use -INF for maxLeftX
            // if partitionX is equal to the length of nums1, then there is nothing on the right side,
            // use INF for minRightX
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];

            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                if ((x + y) % 2 == 0)
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / (double)2;
                else
                    return (double)max(maxLeftX, maxLeftY);
            } else if (maxLeftX > minRightY){ // do binary search on the left side of partitionX. Go on left side
                hi = partitionX - 1;
            } else { // maxLeftY > minRightX, do binary search on the right side of partitionY. Go on right side
                lo = partitionX + 1;
            }
        }
        return -1.0;
    }
};

int main(){
    vector<int> nums1 = {2};
    vector<int> nums2 = {};
    cout << Solution::findMedianSortedArrays_2(nums1, nums2);
}

