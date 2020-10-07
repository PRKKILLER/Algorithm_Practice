"""  
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
利用需要delete的node的右子树中的最小值替换

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].
利用需要delete的node的左子树的最大值替换

    5
   / \
  2   6
   \   \
    4   7
"""

"""  
BST的题目可以先想想 递归 的思路，因为BST任意节点的subtree也是BST
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """  
    当找到需要delete的Node时，用该node的右子树中的最小值替换该节点
    并删除该节点右子树中的被替换的节点
    """
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            
            # if root.right exists, find the min value in the right subtree
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
                
            root.val = tmp.val
            
            # delete the tmp node in the right subtree
            root.right = self.deleteNode(root.right, root.val)

        return root

    def deleteNode2(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            
            # if the root.left exists, find the max value in the left subtree
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
                
            root.val = tmp.val
            
            # we replace the root.val with tmp.val
            # now we want to delete the tmp node
            root.left = self.deleteNode(root.left, tmp.val)
        
        return root