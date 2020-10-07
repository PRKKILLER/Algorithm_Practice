"""  
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

# ord(char) = char的ASCII码值
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            res = res * 26 + (ord(i) - 65 + 1) # ord('A') = 65
            
        return res