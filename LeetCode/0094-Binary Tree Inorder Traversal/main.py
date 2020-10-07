# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        inorder = []
        stk = []
        while True:
            while root:
                stk.append(root)
                root = root.left
            
            if not stk:
                break
            
            # 当前节点不存在左子树或已经访问过
            root = stk.pop()
            inorder.append(root.val)
            root = root.right
        
        return inorder