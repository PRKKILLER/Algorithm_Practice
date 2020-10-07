"""
Given an array arr, replace every element in that array with the greatest element among 
the elements to its right, and replace the last element with -1.

After doing so, return the array.


Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""

# 思路：从右向左遍历数组，并且维护一个maxR变量保存右侧最大值
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxR, n = arr[-1], len(arr)
        for i in range(n-2, -1, -1):
            tmp = arr[i]
            arr[i] = maxR
            maxR = max(tmp, maxR)
        
        arr[-1] = -1
        return arr