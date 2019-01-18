class Solution(object):
    '''
    Given an integer, write a function to determine if it is a power of two.
    '''

    # 利用2 ^ 31 判断
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 2 ** 31 % n == 0


print(Solution().isPowerOfTwo(536870912))
