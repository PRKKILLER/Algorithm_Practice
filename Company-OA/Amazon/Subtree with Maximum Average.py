"""  
Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants. 
The average value of a subtree is the sum of its values, divided by the number of nodes.

Example 1:

Input:
		 20
	   /   \
	 12     18
  /  |  \   / \
11   2   3 15  8

Output: 18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

18 has the maximum average so output 18.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []

class Solution:
    def MaxAverageSubtree(self, root: TreeNode):
        if not root or not root.children: return None

        # res[0]: average; res[1]: target nodes
        self.res = [float('-inf'), None]
        self.dfs(root)
        return self.res[1]

    def dfs(self, root: TreeNode):
        if not root.children:
            return [root.val, 1]
        
        tmp_sum, tmp_num = root.val, 1
        for child in root.children:
            child_sum, child_num = self.dfs(child)
            tmp_sum += child_sum
            tmp_num += child_num

        if tmp_sum / tmp_num > self.res[0]:
            self.res = [tmp_sum / tmp_num, root]
        
        return [tmp_sum, tmp_num]