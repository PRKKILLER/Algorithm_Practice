"""  
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves 
exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True
"""

class Solution:
    """  
    1. 方法1： Top-down approach
    对于任意moment (x, y), 它有两个选择进行状态转移:
    (1) (x, x+y)
    (2) (x+y, x)

    这就构成了二叉树
    
    """
    def reachingPoints(self, sx, sy, tx, ty):
        if sx == tx and sy == ty:
            return True
        
        if sx > tx or sy > ty:
            return False

        return self.reachingPoints(sx, sx + sy, tx, ty) or self.reachingPoints(sx + sy, sy, tx, ty)


    """  
    2. 方法2： Bottom-up approach
    观察可知，对于任意child node, 只有一条路可以reach its parent，eventually to the root of the binary tree
    这就意味着，我们不需要从(sx, sy)出发，而是从(tx, ty)出发，一直向上搜索，直到碰到 conditions like: sx >= tx or sy >= ty
    """

    def reachingPoints2(self, sx, sy, tx, ty):
        while sx < tx and sy < ty:
            if tx < ty:
                ty %= tx
            else:
                tx %= ty

        if sx == tx and sy <= ty and (ty - sy) % sx == 0:
            return True

        if sy == ty and sx <= tx and (tx - sx) % sy == 0:
            return True

        return False
