"""  
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
"""

from typing import List


class Solution:
    """  
    Bottom-up DP Solution: 2 round
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # start at index=0
        p, c = 0, cost[0]
        for i in range(2, n + 1):
            tmp = c
            c = min(p + cost[i - 2], c + cost[i - 1])
            p = tmp

        # start at index=1
        f, g = 0, cost[1]
        for i in range(3, n + 1):
            tmp = g
            g = min(f + cost[i - 2], g + cost[i - 1])
            f = tmp

        return min(c, g)

    """  
    Bottom-up DP solution (Tabulation)
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[-1]

    """  
    Top-bottom DP solution with Memoization
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        def min_cost(idx: int):
            # base case
            if idx <= 1:
                return 0

            if dp[idx]:
                return dp[idx]

            down_one = min_cost(idx - 1)
            down_two = min_cost(idx - 2)
            dp[idx] = min(down_one, down_two)
            return dp[idx]

        return min_cost(n)
