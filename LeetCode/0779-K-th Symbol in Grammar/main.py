"""
On the first row, we write a 0. Now in every subsequent row, 
we look at the previous row and replace each occurrence of 0 with 01, 
and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. 
(The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
"""

class Solution:
    # not accepted, tle
    def kthGrammar(self, N: int, K: int) -> int:
        prev = [0]
        for i in range(1, N):
            cur = []
            for j in prev:
                cur.extend([0,1] if j == 0 else [1, 0])
            prev = cur
        
        return prev[K-1]

    # 思路：将整个问题看作是一个binary tree，第N行的第K个值其实就是完全binary tree在第N层的第K个节点
    # 当K是even时，它是r-child，它的父节点在上一层的位置 = K/2; 
    # 当K是odd时，它是l-child，它的父节点在上一层的位置 = (K+1)/2
    # 通过观察可知，第K个节点的值是由它父节点的值决定的，以此类推，就可以用递归解决该问题
    def kthGrammar2(self, N: int, K: int) -> int:
        if N == 1: return 0 # root节点
        if k % 2: # K为l-child
            parent = self.kthGrammar2(N-1, (K+1)/2)
            if parent == 0: return 0
            else: return 1
        else: #K为r-child
            parent = self.kthGrammar2(N-1, K/2)
            if parent == 0: return 1
            else: return 0