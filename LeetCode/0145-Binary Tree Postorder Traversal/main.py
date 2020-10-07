# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        postorder = []
        stk = [root]
        while stk:
            root = stk.pop()
            postorder.insert(0, root.val) #头插，让其倒序输出
            if root.left:
                stk.append(root.left)
            
            if root.right:
                stk.append(root.right)
            
        return postorder