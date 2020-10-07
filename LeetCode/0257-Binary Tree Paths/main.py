"""  
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        
        self.res = []
        self.dfs(root, [])
        return ['->'.join(path) for path in self.res]
        
    def dfs(self, node, arr):
        arr = arr[:]
        arr.append(str(node.val))
        if not node.left and not node.right:
            self.res.append(arr)
        
        if node.left:
            self.dfs(node.left, arr)
        if node.right:
            self.dfs(node.right, arr)