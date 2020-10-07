"""  
Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so 
that the string becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.


Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Example 2:

Input: palindrome = "a"
Output: ""

Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n < 2: return ''
        
        mid = n // 2
        palindrome = list(palindrome)

        for i in range(mid):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        
        palindrome[-1] = 'b'  # 当palindrome前半部分都为'a'时，将最后一位改为'b'
        
        return ''.join(palindrome)