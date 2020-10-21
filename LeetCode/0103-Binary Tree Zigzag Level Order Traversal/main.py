"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 思路： 还是采用原始的levelorder traversal，
# 但是在奇数层时，每个node的值采用“头插”
# 偶数层时，每个node的值采用尾插法
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        from collections import deque
        res = []
        q = deque([root])
        is_odd = False
        
        while q:
            sz = len(q)
            level = deque()
            for i in range(sz):
                node = q.popleft()
                if is_odd:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(list(level))
            is_odd = not is_odd
        
        return res
