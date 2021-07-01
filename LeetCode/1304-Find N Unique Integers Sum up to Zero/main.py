"""  
Given an integer n, return any array containing n unique integers such that they add up to 0.


Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]

"""


class Solution:
    # find symmetric number pairs
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2:
            res.append(0)
            n -= 1

        n //= 2
        while n > 0:
            res.extend([-n, n])
            n -= 1

        return res
