"""  
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to 
each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
"""
from collections import Counter


"""  
first sort the letter in S by frequency, find the largest occurrence
if largest occurrence > (len(S) + 1) // 2, it's impossible to form the new string, return ''
Otherwise, put the letter into even index number (0, 2, 4 ...) char array
when the index >= len(S), put the rest of the letter at odd index number (1,3,5...)

Consider this example: "aaabbbcdd", we will construct the string in this way:

a _ a _ a _ _ _ _ // fill in "a" at position 0, 2, 4
a b a _ a _ b _ b // fill in "b" at position 6, 8, 1
a b a c a _ b _ b // fill in "c" at position 3
a b a c a d b d b // fill in "d" at position 5, 7
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2: return S
        
        tmp = list(dict(Counter(S)).items()) 
        tmp = sorted(tmp, key=lambda x: x[1], reverse=True) # sort by frequency
        letter, cnt = tmp[0][0], tmp[0][1]
        n = len(S)
        if cnt > (n + 1) // 2: return ''
        
        res = [None] * n
        # 先将相同字符放在偶数位：0，2，4，8...
        # 偶数位放满了，放奇数位
        idx = 0
        for item in tmp:
            letter, cnt = item[0], item[1]

            for i in range(cnt):
                if idx >= n:
                    idx = 1
                res[idx] = letter
                idx += 2
        
        return ''.join(res)