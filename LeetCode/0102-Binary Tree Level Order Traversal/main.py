from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        levelorder = []
        q = Queue()
        q.put(root)
        while not q.empty():
            cur_len = q.qsize()
            one_level = []
            for i in range(cur_len):
                node = q.get()
                one_level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            levelorder.append(one_level)
        
        return levelorder
