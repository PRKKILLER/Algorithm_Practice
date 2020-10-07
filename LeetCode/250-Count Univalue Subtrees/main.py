"""  
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: TreeNode):
        if not root: return 0

        cnt = 0
        q = deque([root])
        while q:
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                if not node.left and not node.right:
                    cnt += 1
                elif node.left and not node.right:
                    q.append(node.left)
                elif not node.left and node.right:
                    q.append(node.right)
                else:
                    if node.left.val == node.right.val:
                        cnt += 1
                    q.append(node.left)
                    q.append(node.right)
        
        return cnt

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(1, TreeNode(5), TreeNode(5))
    root.right = TreeNode(5, None, TreeNode(5))
    print(sol.countUnivalSubtrees(root))