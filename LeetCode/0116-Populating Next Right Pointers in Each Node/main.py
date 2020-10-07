"""
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space 
for this problem.
"""


# Definition for a Node.

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:

    def connect(self, root: Node) -> Node:
        if not root:
            return root
        
        pre, cur = root, None
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        
        return root

    # 递归
    def connect2(self, root: Node):
        self.dfs(root, None)
        return root
    
    def dfs(self, cur: Node, next: Node) -> None:
        if not cur:
            return

        cur.next = next
        self.dfs(cur.left, cur.right)
        if cur.next:
            self.dfs(cur.right, cur.next.left)
        else:
            self.dfs(cur.right, None)

    def connect3(self, root: Node):
        if not root or not root.left:
            return root

        q = [root]
        while q:
            cur_len = len(q)
            for i in range(cur_len - 1):
                q[i].next = q[i+1]

            for i in range(cur_len):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
        
        return root
