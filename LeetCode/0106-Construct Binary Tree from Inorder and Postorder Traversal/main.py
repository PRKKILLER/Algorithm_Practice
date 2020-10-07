"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
基本思想： 分而治之

1. postorder traversal 的顺序是：左-右-根，因此可以通过postorder的最后一个元素得到tree的root节点
2. 下一步，我们想知道，root节点的left child 和 right child
3. inorder traversal 顺序是：左-根-右，且题目给出了重要的条件就是不存在duplicate，则可以通过 inorder.index(root.val)
   得到root节点在 inorder 中的位置。root节点将inorder分为了两部分，左子树和右子树
4. 既然我们知道根元素是哪一个，利用中序数组，我们就知道了左子树有多少个元素，右子树有多少个元素。
拿着这两个数据，回到后序数组，我们就能把后序数组分为三个部分：

[左子树的节点们][右子树的节点们][根]

这样，根据性质1，就找到了根节点的左右子节点。
重复上述步骤，你就得到了一棵二叉树。
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
    
    def helper(self, inorder, iLeft, iRight, postorder, pLeft, pRight):
        if iLeft > iRight or pLeft > pRight:
            return None
        
        node = TreeNode(postorder[pRight])
        idx = inorder.index(node.val)
        len_left_tree = idx - iLeft
        
        node.left = self.helper(inorder, iLeft, idx - 1, 
                                postorder, pLeft, pLeft + len_left_tree - 1)
        node.right = self.helper(inorder, idx + 1, iRight, 
                                postorder, pLeft + len_left_tree, pRight - 1)
        
        return node