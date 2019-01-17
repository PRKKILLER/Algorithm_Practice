class Solution(object):
    '''
    Count the number of prime numbers less than a non-negative number, n.
    '''

    # 利用 Sieve_of_Eratosthenes 算法
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True] * n # 初始化一个素数表，一开始假设所有数均为

        i = 2
        while i ** 2 < n:
            if isPrime[i]:
                j = i ** 2
                while j < n: # 循环查找所有小于n的i的倍数，并且标记为FALSE
                    isPrime[j] = 0
                    j += i
            i += 1

        return sum(isPrime[2:])

    # more pythonic way to write the code
    def countPrimes_v2(self, n):
        """
            :type n: int
            :rtype: int
        """
        if n < 2:
            return 0

        import numpy as np
        isPrime = np.ones(n, dtype=bool)
        for i in range(2, int(n ** 0.5) + 1): # iterate between(2, sqrt(n) + 1)
            if isPrime[i]:
                isPrime[i ** 2: n: i] = False
        return int(np.sum(isPrime[2:]))

print(type(Solution().countPrimes_v2(3)))
print(type(3))