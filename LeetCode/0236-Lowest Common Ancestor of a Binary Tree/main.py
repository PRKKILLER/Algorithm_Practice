"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p == root.val or q == root.val:
            return root

        m = {root: root}
        stk = [root]
        # p_level, q_level分别存放p,q在二叉树中所在的层数
        p_level = q_level = level = 0
        while stk:
            cur_len = len(stk)
            level += 1
            for i in range(cur_len):
                node = stk.pop(0)
                if node.left:
                    m[node.left] = node
                    stk.append(node.left)
                    if node.left.val == p.val:
                        p_level = level + 1
                    elif node.left.val == q.val:
                        q_level = level + 1

                if node.right:
                    m[node.right] = node
                    stk.append(node.right)
                    if node.right.val == p.val:
                        p_level = level + 1
                    elif node.right.val == q.val:
                        q_level = level + 1

            if p_level and q_level:
                break

        if p_level > q_level:
            diff = p_level - q_level
            for i in range(diff):
                p = m[p]
        elif p_level < q_level:
            diff = q_level - p_level
            for i in range(diff):
                q = m[q]

        if p.val == q.val:
            return p
        
        while m[p].val != m[q].val:
            p = m[p]
            q = m[q]

        return m[p]

    @staticmethod
    def lowestCommonAncestor2(root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q:
            return root

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop(0)

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    ans = Solution.lowestCommonAncestor(root, root.left.right.right, root.left)
    print(ans.val)