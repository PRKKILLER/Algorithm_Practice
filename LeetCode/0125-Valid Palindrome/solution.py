import re
class Solution:
    '''
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
    '''

    # 利用正则表达式
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        s = ''.join(re.split(r'[^A-Za-z0-9]', s.lower())) # 以''连接List的每一个元素
        return s == s[::-1]


    def isPalindrome_v2(self, s):
        """
            :type s: str
            :rtype: bool
        """
        if not s:
            return None

        s = [x for x in s.lower() if x.isalnum()]
        return s == s[::-1]


test = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(test)