"""  
Given two integer arrays arr1 and arr2, and the integer d, 
return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] 
such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.


Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
"""

"""  
该题的目的是对于 arr1 中的每一个数字，让它和 arr2 中的每一个数字进行比较，若最小的差值 > d，则将 distance ＋ 1;

该题最直接的做法是 brute force，O(MN); 
但是该题也可以使用 binary search，让时间复杂度优化为 O(MlogN)。我们首先对 arr2进行排序，
并且利用 binary search 在 arr2 中 arr1[i] 的 closest element 
"""




from typing import List
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        m, n = len(arr1), len(arr2)
        arr2.sort()

        # binsearch for the closest element
        def binSearch(target: int) -> int:
            if target <= arr2[0]:
                return arr2[0]

            if target >= arr2[-1]:
                return arr2[-1]

            lo, hi = 0, n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if target <= arr2[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # important, since searched results arr2[lo] >= target,
            # we need to compare arr2[lo - 1] and arr2[lo] to see
            # which one is the closest element to the target

            if target - arr2[lo - 1] < arr2[lo] - target:
                return arr2[lo - 1]

            return arr2[lo]

        res = 0
        for num in arr1:
            closest = binSearch(num)
            res += (abs(num - closest) > d)

        return res
