from collections import deque, defaultdict
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        # 存储 x -> node_list 映射
        # 结构：key: int; value: list 
        mapping = defaultdict(list)
        q = deque([(root, 0)])
        x_min, x_max = 0, 0

        while q:
            tmp = defaultdict(list)
            sz = len(q)
            for _ in range(sz):
                node, x = q.popleft()
                tmp[x].append(node.val)
                if node.left:
                    q.append((node.left, x-1))
                    x_min = min(x_min, x-1)
                if node.right:
                    q.append((node.right, x+1))
                    x_max = max(x_max, x+1)
            for k in tmp:
                mapping[k].extend(sorted(tmp[k]))
        
        return [mapping[i] for i in range(x_min, x_max+1)]