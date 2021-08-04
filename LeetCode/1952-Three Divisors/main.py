"""  
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.
"""

"""  
如果一个数有且仅有3个 divisor，则该数一定是完全平方数；且它的平方根为质数
"""


class Solution:
    def isThree(self, n: int) -> bool:
        from math import sqrt
        if n < 4:
            return False

        tmp = int(sqrt(n))
        if tmp ** 2 != n:
            return False

        def isPrime(num: int) -> bool:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    return False

            return True

        return isPrime(tmp)
