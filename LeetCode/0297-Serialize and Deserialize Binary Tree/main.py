"""  
Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string 
can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 利用levelorder traversal
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            res.append(str(node.val) if node else '#')
        
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(',')
        root = TreeNode(int(data[0]))
        idx = 1
        q = deque([root])
        while q:
            node = q.popleft()
            if data[idx] != '#':
                node.left = TreeNode(int(data[idx]))
                q.append(node.left)
            idx += 1

            if data[idx] != '#':
                node.right = TreeNode(int(data[idx]))
                q.append(node.right)
            idx += 1

        return root

# 利用递归的preorder traversal
class Codec2:
    def serialize(self, root):
        def doit(node):
            if node:
                res.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                res.append('#')

        res = []
        doit(root)
        return ','.join(res)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split(','))
        root = doit()
        return root

# 递归: inorder traversal
# 不可以
class Codec3:
    def serialize(self, root):
        def doit(node):
            if not node: 
                res.append('#')
                return
            doit(node.left)
            res.append(str(node.val))
            doit(node.right)
    
        res = []
        doit(root)
        return ','.join(res)

    def deserialize(self, data):
        pass
        # 无法实现，因为无法在序列化的data中找到root节点的位置