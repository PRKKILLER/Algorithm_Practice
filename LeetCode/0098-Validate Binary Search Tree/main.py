"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：若一个Binary tree是Binary Search Tree, 则对其进行中序遍历的话
# 中序遍历的结果是有小到大顺序严格递增的。
# 因此判断一个二叉树是否真的是BST，就对其进行中序遍历，若发现上一个节点的值>=当前节点，就返回FALSE
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True
        
        inorder = float('-inf')
        stk = []
        while True:
            while root:
                stk.append(root)
                root = root.left  
            if not stk:
                break
            root = stk.pop()
            if inorder >= root.val:
                return False
            inorder = root.val
            root = root.right
            
        return True