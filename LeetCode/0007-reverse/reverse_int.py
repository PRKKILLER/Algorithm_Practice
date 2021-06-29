class Solution:
    '''
    Given a 32-bit signed integer, reverse digits of an integer.
    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
    range: [−231,  231 − 1]. 
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
    '''

    def reverse_s1(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        temp = abs(x)  # 中间变量
        sign = 1 if x >= 0 else -1  # 符号位
        while temp:
            res = res * 10 + temp % 10  # 对x取余数，得到最低位
            temp = temp // 10  # 对x整除10，消除最低位

        return sign * res * (res < 2 ** 31)  # 注意这里的trick， 可以省略一个if判断

    # 利用字符串进行求解
    def reverse_s2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1 * self.reverse_s2(-x)

        x_reverse = int(str(x)[::-1])
        return x_reverse * (x_reverse < 2 ** 31)

    def revers_3(self, x):
        sign = 1 if x >= 0 else -1
        x_reverse = int(str(sign * x)[::-1])
        return sign * x_reverse * (x_reverse < 2 ** 31)
