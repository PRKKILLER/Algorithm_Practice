"""
Given an array A of non-negative integers, half of the integers in A are odd, 
and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.


Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = [], []
        for num in A:
            if num % 2:
                odd.append(num)
            else:
                even.append(num)
                
        cnt = 0
        for i in range(len(even)):
            A[cnt], A[cnt+1] = even[i], odd[i]
            cnt += 2
        
        return A

    # in-place onepass solution
    # 因为数组的长度为偶数，且一半为偶数，一半为奇数
    # 因此对于每一个错位的偶数项，就一定有一项错位的奇数项与之相对应
    # 此算法的精妙之处就在于采用 if, elif判断，
    # 只有当i，j两个位置上的数字都misplaced，才会进入最后一个else条件
    def sortArrayByParityII2(self, A):
        i = 0 # pointer for misplaced even
        j = 1 # pointer for misplaced odd
        n = len(A)
        while i < n and j < n:
            if A[i] % 2 == 0:
                i += 2
            elif A[j] % 2 == 1:
                j += 2
            else:
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
        
        return A