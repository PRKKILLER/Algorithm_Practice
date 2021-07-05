"""  
source: https://www.lintcode.com/problem/349/description

Description
A software company is forming teams that consist of a specific number of employees. 
There are two types of employees: software developers and software testers. 
They want to make sure the developers and testers are well-integrated, 
so they decide to limit the number of testers and developers that can be seated consecutively 
with employees of the same type. 
Given the desired team size and these limits, how many different ways can the company form a team?

Note: The number of ways could be very large, so return it modulo 10^9 + 7


Example 1

Input:
d = 2
t = 2
queries = [2, 5, 7, 11]
Output: [2, 2, 2, 2]
Explanation: Here, d = 2, t = 2, and there are 4 queries regarding team size: [2, 5, 7, 11]. Here are the possible ways to form the teams:
- n = 2: DT, TD
- n = 5: DTDTD, TDTDT
- n = 7, DTDTDTD, TDTDTDT
- n = 11, DTDTDTDTDTD, TDTDTDTDTDT
"""


class Solution:
    """
    @param d:  limit the number of developers that can be seated consecutively with employees of the same type
    @param t:  limit the number of testers that can be seated consecutively with employees of the same type
    @param queries: the queries of team size 
    @return: return the number of ways
    """

    def theNumberofWays(self, d, t, queries):
        maxSize = max(queries)
        d_dp = [0] * (maxSize + 1)
        t_dp = [0] * (maxSize + 1)
        d_dp[0] = 1
        t_dp[0] = 1
        d_dp[1] = 1
        t_dp[1] = 1
        MOD = 10 ** 9 + 7

        for i in range(2, maxSize + 1):
            d_dp[i] = d_dp[i - 1] + t_dp[i - 1] - \
                (t_dp[i - d] if i >= d else 0)
            d_dp[i] %= MOD
            t_dp[i] = t_dp[i - 1] + d_dp[i - 1] - \
                (d_dp[i - t] if i >= t else 0)
            t_dp[i] %= MOD

        ans = []
        for q in queries:
            ans.append((d_dp[q] + t_dp[q]) % MOD)

        return ans
