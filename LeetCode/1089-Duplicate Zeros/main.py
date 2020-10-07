"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, 
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.



Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""

class Solution:
    # 思路：遍历数组，若遇到0，则将arr中0之后的部分保存，用于将数据内容右移
    # 注意判断在加0之后是否越界
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, length = 0, len(arr)
        while i < length:
            if arr[i] != 0:
                i += 1
            else:
                if i + 1 == length:
                    return
                
                tmp = arr[i+1:-1] # 暂存数组剩余部分内容
                arr[i+1] = 0
                if i + 2 == length:
                    return 

                arr[i+2:] = tmp
                i += 2
