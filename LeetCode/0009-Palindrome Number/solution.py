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

test = Solution().isPalindrome(-121)
print(test)

