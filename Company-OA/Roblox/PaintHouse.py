"""  
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
The cost of painting each house with a certain color is different. You have to paint all the houses such that 
no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of 
painting house 1 with color green, and so on... 
Find the minimum cost to paint all houses.
"""

"""  
思路：维护1个二维dp数组，则dp[i][j]表示刷第i+1个房子用颜色j的最小花费
"""

def solution(costs):
    dp = costs.copy()
    for i in range(1, len(dp)):
        dp[i][0] += min(dp[i-1][1], dp[i-1][2])
        dp[i][1] += min(dp[i-1][0], dp[i-1][2])
        dp[i][2] += min(dp[i-1][0], dp[i-1][1])
    
    return min(dp[-1])

costs = [[17,2,17],[16,16,5],[14,3,19]]
print(solution(costs))