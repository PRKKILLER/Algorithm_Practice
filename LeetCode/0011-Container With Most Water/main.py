"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Example:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
"""


class Solution:
    # approach 1: two-pointers (greedy)
    # we start by positioning at the begining and end of the height list,
    # and get the maxmum width; than moving pointers to get the maximum area
    # Time complexity: O(N)
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        res = min(height[lo], height[hi]) * hi

        while lo < hi:
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
            res = max(res, min(height[lo], height[hi]) * (hi-lo))

        return res
