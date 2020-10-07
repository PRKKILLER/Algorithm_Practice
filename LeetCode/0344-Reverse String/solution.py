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

    def reverseString2(self, s):
        if len(s) < 2:
            return s
        
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]