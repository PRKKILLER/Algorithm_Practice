class Solution:
    '''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.
    '''
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(' ').split(' ') # 先用s.strip(' ')去掉末尾的空格
        return len(s[-1])

test = Solution().lengthOfLastWord('a ')
print(test)