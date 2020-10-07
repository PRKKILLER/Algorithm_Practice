"""  
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。
我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 
是不允许的。 
"""

class Solution:
    """  
    本题思路和lc875的猴子吃香蕉其实是一样的。船的每一个capacity对应一个运货天数
    因为每个货物不能分开运输，因此为了保证船能够运送所有的货物，min_capacity=max(weights)
    max_capacity = sum(weights)
    然后利用二分法查找，计算出某个capacity 对应的运货天数
    """
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo, hi = max(weights), sum(weights) + 1
        while lo < hi:
            mi = (lo + hi) // 2
            if self.shipTime(mi, weights) <= D:
                hi = mi
            else:
                lo = mi + 1
        
        return lo
    
    def shipTime(self, cap, weights):
        cnt, tmp = 0, 0
        for item in weights:
            tmp += item
            if tmp > cap:
                cnt += 1
                tmp = item
                
        return cnt + 1