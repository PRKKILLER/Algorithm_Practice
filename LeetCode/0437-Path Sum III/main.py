"""  
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards 
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.preSum = collections.defaultdict(int)

    # 时间复杂度：O(n)，核心思想：前缀和
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        
        self.preSum[0] = 1
        return self.pathFinder(root, 0, sum)

    def pathFinder(self, node: TreeNode, curSum, target: int) -> int:
        if not node: return 0
        
        curSum += node.val
        numOfPath = self.preSum[curSum - target]
        self.preSum[curSum] += 1
        
        res = numOfPath + self.pathFinder(node.left, curSum, target) \
                + self.pathFinder(node.right, curSum, target)
        
        self.preSum[curSum] -= 1
        
        return res

    #####################################################
    # 基本思想：dfs 时间复杂度: O(n^2)
    def pathSum2(self, root: TreeNode, target: int) -> int:
        if not root: return 0

        return self.pathSumFrom(root, target) + self.pathSum2(root.left) + \
            self.pathSum2(root.right)

    # 返回以node为根节点，sum=target的总路径
    def pathSumFrom(self, node: TreeNode, target: int) -> int:
        if not node: return 0

        curPath = 1 if node.val == target else 0
        return curPath + self.pathSumFrom(node.left, target - node.val) + \
            self.pathSumFrom(node.right, target - node.val)

