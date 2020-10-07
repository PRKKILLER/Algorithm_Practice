"""  
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt = 0
        stk, cur = [], root
        
        while True:
            while cur:
                stk.append(cur)
                cur = cur.left
            if not stk:
                break
            p = stk.pop()
            cnt += 1
            if cnt == k:
                return p.val
            
            cur = p.right