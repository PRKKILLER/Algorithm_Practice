class Solution(object):
    '''
    Write a function that takes a string as input and returns the string reversed.
    '''
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


print(Solution().reverseString('A man, a plan, a canal: Panama'))