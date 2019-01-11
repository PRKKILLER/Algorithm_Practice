class Solution:
    '''
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer,
the decimal digits(小数部分) are truncated（截断） and only the integer part of the result is returned.
    '''

    # 运用binary search
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            raise Exception('please use non-negative number')
        elif x == 1:
            return x
        else:
            left, right = 0, x
            while left <= right:
                mid = (left + right) // 2
                if mid ** 2 <= x < (mid + 1) ** 2:
                    return mid
                elif x < mid ** 2:
                    right = mid
                else:
                    left = mid
