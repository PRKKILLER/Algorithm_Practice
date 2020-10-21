"""  
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == root or q == root:
            return root
        
        # p, q 在 root两侧，返回root
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        elif p.val < root.val: # p, q 均小于root，在root的左子树继续寻找
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val: # p, q 均大于root，在root的右子树继续寻找
            return self.lowestCommonAncestor(root.right, p, q)