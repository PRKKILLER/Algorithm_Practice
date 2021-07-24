"""  
Given an array of non-negative integers nums, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.


Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

"""

from enum import Enum


class Index(Enum):
    Undefined = 0
    Good = 1
    Bad = 2


class Solution:
    """  
    Approach 1: Top-bottom DP solution
    Good observation: Once we determain a certain index is good or bad, this will never change
    So we can use memoization technique to store whether certain index is good or bad.
    """

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [Index.Undefined] * n
        memo[-1] = Index.Good

        def canJumpFromIdx(idx: int):
            if memo[idx] != Index.Undefined:
                return True if memo[idx] == Index.Good else False

            farthest_pos = min(idx + nums[idx], n - 1)

            for p in range(idx + 1, farthest_pos):
                if canJumpFromIdx(p):
                    memo[p] = Index.Good
                    return True

            memo[idx] = Index.Bad
            return False

        return canJumpFromIdx(0)

    """  
    Approach 2: Bottom-up DP solution
    Good observation: we can determain certain index is good or bad only
    based on the indexes on the right side of the current one

    时间复杂度: O(N^2)
    """

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [Index.Undefined] * n
        memo[-1] = Index.Good

        for idx in range(n - 2, -1, -1):
            farthest_pos = min(idx + nums[idx], n - 1)

            for p in range(idx + 1, farthest_pos + 1):
                if memo[p] == Index.Good:
                    memo[idx] = Index.Good
                    break

        return memo[0] == Index.Good

    """  
    Approach 3: Greedy
    Good observation: 

    From a given position, when we try to see if we can jump to a GOOD position, 
    we only ever use one - the first one (see the break statement). In other words, the left-most one. 
    If we keep track of this left-most GOOD position as a separate variable, 
    we can avoid searching for it in the array. 
    
    Not only that, but we can stop using the array altogether.

    Iterating right-to-left, for each position we check if there is a potential jump 
    that reaches a GOOD index (currPosition + nums[currPosition] >= leftmostGoodIndex). 
    If we can reach a GOOD index, then our position is itself GOOD. 
    Also, this new GOOD position will be the new leftmost GOOD index. 
    Iteration continues until the beginning of the array. 
    If first position is a GOOD index then we can reach the last index from the first position.
    """

    def canJump(self, nums: List[int]) -> bool:
        left_most_good_idx = len(nums) - 1

        for idx in range(len(nums) - 2, -1, -1):
            if idx + nums[idx] >= left_most_good_idx:
                left_most_good_idx = idx

        return left_most_good_idx == 0
