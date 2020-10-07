"""
Given an array arr of integers, 
check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for num in arr:
            if num * 2 in s or (num % 2 == 0 and num // 2 in s):
                return True
            s.add(num)
        
        return False
        