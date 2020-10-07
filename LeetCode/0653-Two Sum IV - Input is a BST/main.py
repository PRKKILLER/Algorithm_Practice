"""  
Given a Binary Search Tree and a target number, 
return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""  
思路：BST的中序遍历结果就是从小到大排列的数组
因此首先通过中序遍历得到有序数组，然后利用双指针i, j从数组两侧搜索，是否存在i, j符合条件
"""
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def traversal(root):
            if root.left: traversal(root.left)
                
            inorder.append(root.val)
            
            if root.right: traversal(root.right)
        
        if not root: return False
        
        inorder = []
        traversal(root)
        i, j = 0, len(inorder) - 1
        
        while i < j:
            tmp = inorder[i] + inorder[j]
            if tmp < k:
                i += 1
            elif tmp > k:
                j -= 1
            else:
                return True
            
        return False