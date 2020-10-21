"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]

Explanation: Given the above binary tree (Figure A), 
your function should populate each next pointer to point to its next right node, 
just like in Figure B. The serialized output is in level order as connected by the next pointers, 
with '#' signifying the end of each level.
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class solution:
    def connect(self, root: Node):
        if not root:
            return root
        
        cur = root
        dummy = p = Node(-1)
        while cur:
            if cur.left:
                p.next = cur.left
                p = p.next
            if cur.right:
                p.next = cur.right
                p = p.next
            
            if cur.next:
                cur = cur.next
            else:
                cur = dummy.next # 下一层的第一个节点
                dummy.next = None
                p = dummy

        return root

    def connect2(self, root: Node):
        if not root:
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
                if node.right:
                    q.append(node.right)

        return root

