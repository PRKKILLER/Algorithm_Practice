# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 利用stack先进后出的性质，每次右子树的根节点先入栈
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        preorder = []
        stk = [root]

        while stk:
            root = stk.pop()
            preorder.append(root.val)
            if root.right:
                stk.append(root.right)
            
            if root.left:
                stk.append(root.left)

        return preorder

    # 利用辅助栈，先访问left vine，再转向右子树
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        preorder = []
        stk = []

        while True:
            while root:
                preorder.append(root.val)
                if root.right: # 右子树入栈保存
                    stk.append(root.right)
                root = root.left # 不断向左子树深入
            if not stk:
                break
            root = stk.pop() # 转向右子树
        
        return preorder


    # 递归方法
    def preorderTraversal_trivial(self, root: TreeNode) -> List[int]:
        preorder = []
        self.trav_recursive(root, preorder)
        return preorder

    def trav_recursive(self, p: TreeNode, v: list):
        if not p:
            return

        v.append(p.val)
        self.trav_recursive(p.left, v)
        self.trav_recursive(p.right, v)
