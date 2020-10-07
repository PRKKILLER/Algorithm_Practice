"""
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, also in sorted non-decreasing order.


Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution:
    # 时间复杂度为O(n)的解题思路：
    # 从abs(x)的角度上看，array A两端的数字最大，并且不断向数组中间收敛
    # 因此可以利用“双指针”的思路，从两端扫描数组
    # 时间复杂度：O(n)，空间复杂度：O(1)

    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        lo, hi = 0, len(A) - 1
        while lo <= hi:
            left, right = A[lo] ** 2, A[hi] ** 2
            if left > right:
                res.append(left)
                lo += 1
            else:
                res.append(right)
                hi -= 1
        return (res[::-1])
