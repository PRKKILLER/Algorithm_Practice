"""  
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, 
but instead be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        
        res = []
        cnt = 1
        
        for i in range(len(chars) - 1):
            if chars[i] == chars[i+1]:
                cnt += 1
            else:
                if cnt == 1:
                    res.append(chars[i])
                else:
                    res.extend([chars[i]] + list(str(cnt)))
                cnt = 1
                
        if cnt == 1:
            res.append(chars[-1])
        else:
            res.extend([chars[i]] + list(str(cnt)))
            
        n = len(res)
        chars[:n] = res
        return n