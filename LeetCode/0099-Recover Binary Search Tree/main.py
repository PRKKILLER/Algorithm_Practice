"""  
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # BST的中序遍历结果就是节点从小到大的排序结果
        # 利用该性质找到misplaced节点
        self.first = None # 第一个错位节点
        self.second = None # 第二个错位节点
        self.pre = None # 指向前一个节点
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    # inorder traversal
    def dfs(self, root: TreeNode) -> None:
        if root.left: 
            self.dfs(root.left)
        
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            
            if self.first:
                self.second = root
        
        self.pre = root
        if root.right:
            self.dfs(root.right)