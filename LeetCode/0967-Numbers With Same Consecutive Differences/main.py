"""  
Return all non-negative integers of length N such that the absolute difference between every 
two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. 
For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.


Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
"""

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        """
        思路：dfs，建立prevDigit和currentDigit之间的关系:
        
        if prevDigit + K < 10: currentDigit = prevDigit + 10
        if prevDigit - k >= 0: currentDigit = prevDigit - 10 

        当 K == 0时, prevDigit + K == prevDigit - k >= 0，只需dfs一次
        """
        if N == 1:
            return list(range(10))
        
        digits = range(1, 10)
        res = []
        for d in digits:
            self.dfs(d, N - 1, K, res)
            
        return res
    
    def dfs(self, num, N, K, res):
        if N == 0: 
            res.append(num)
            return
        
        last = num % 10 # 取得当前数字最低位
        if last + K < 10:
            self.dfs(num * 10 + last + K, N - 1, K, res)
        
        if K > 0 and last - K >= 0:
            self.dfs(num * 10 + last - K, N - 1, K, res)