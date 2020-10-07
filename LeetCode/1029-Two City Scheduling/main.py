"""  
There are 2N people a company is planning to interview. 
The cost of flying the i-th person to city A is costs[i][0], 
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.


Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
"""

"""  
思路：首先计算出 2N 个人到城市 A 的 totalCost
再计算出 每个人 到B城市与到A城市的差价，从小打大排序
再将前 N 个差价与totalCost相加，即为最低的价格
"""
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalCost, n = 0, len(costs)
        # 计算出送n个人到A city 的 total cost
        for i in costs:
            totalCost += i[0]
        
        # 计算送每个人到B和到A的费用差
        # item < 0 表示到B更便宜，item > 0表示去A更便宜
        # 再从小到大排序
        refund = sorted([cost[1] - cost[0] for cost in costs])
        
        # 送一半的人去B
        for i in range(n // 2):
            totalCost += refund[i]
            
        return totalCost