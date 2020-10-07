class Solution:
    '''
    Determine whether an integer is a palindrome.(回文数）
    An integer is a palindrome when it reads the same backward as forward.

    Example:
        Input: 121 output: True
        Input: -121 output: False
    '''

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

    def isPalindrome_2(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        div = 1
        while x // div >= 10: # div得到x的位数
            div = div * 10
        
        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div = div // 100
        return True

test = Solution().isPalindrome(-22)
print(test)

