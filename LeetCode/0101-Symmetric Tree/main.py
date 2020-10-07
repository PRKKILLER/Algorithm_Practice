# Given a binary tree, check whether it is a mirror of itself

# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        def helper(left, right):
            if not left and not right: return True
            
            if not left or not right: return False
            
            if left.val != right.val: return False
            
            return helper(left.left, right.right) and helper(left.right, right.left)
        
        return helper(root.left, root.right)


    # the essence of recursive is stack, so use our own stack to rewrite it recursively
    def isSymmetric2(self, root: TreeNode):
        from collections import deque
        
        if not root:
            return True
        
        q = deque([(root.left, root.right)])
        while q:
            left,right = q.popleft()
            if not left and not right:
                continue
            if (not left or not right) or (left.val != right.val):
                return False
            
            q.append((left.left, right.right))
            q.append((left.right, right.left))
        
        return True