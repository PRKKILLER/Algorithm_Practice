from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        cache = [0] * 71  # index: temperature; value: day
        res = []
        n = len(T)
        for i in range(n-1, -1, -1):
            temp = T[i] - 30
            if temp == 70:  # 温度为最大值
                res.append(0)
            else:
                days = [x for x in cache[temp+1:] if x]
                if days:
                    res.append(min(days) - i) # 找到temperature比当前大的最小天数
                else:
                    res.append(0)
            cache[temp] = i # 记录气温对应的天数
        
        return res[::-1]

    def dailyTemperatures2(self, T):
        n = lem(T)
        stk = [0] * n
        ret = [0] * n

sol = Solution()
T = [73,74,75,71,69,72,76,73]
res = sol.dailyTemperatures(T)
print(res)