"""  
Given an array of non-negative integers nums, you are initially positioned at the first index 
of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


class Solution:
    """  
    Approach 1: Using BFS to search for the shortest path to the end index
    """

    def jump(self, nums: List[int]) -> int:
        from collections import deque

        dq = deque([0])
        seen = set([0])
        step, n = 0, len(nums)

        while dq:
            sz = len(dq)
            for _ in range(sz):
                pos = dq.popleft()
                if pos == n - 1:
                    return step

                farthest_pos = pos + nums[pos]
                if farthest_pos >= n - 1:
                    return step + 1

                for p in range(pos + 1, farthest_pos + 1):
                    if p in seen:
                        continue
                    dq.append(p)
                    seen.add(p)

            step += 1

        return step
