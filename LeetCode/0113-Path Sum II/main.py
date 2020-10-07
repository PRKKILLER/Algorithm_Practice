"""  
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 基本思路：dfs
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        
        self.res = []
        self.sum = sum
        self.helper(root, 0, [])
        return self.res
    
    def helper(self, node, carry, arr):
        tmp_sum = carry + node.val
        arr = arr[:]
        arr.append(node.val)
        if not node.left and not node.right and tmp_sum == self.sum:
            self.res.append(arr)
            return
        
        if node.left:
            self.helper(node.left, tmp_sum, arr)
        if node.right:
            self.helper(node.right, tmp_sum, arr)