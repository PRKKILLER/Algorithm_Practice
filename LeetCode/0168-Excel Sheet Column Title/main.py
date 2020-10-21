"""  
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
"""

"""  
Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

But how to get the column title from the number? We can't simply use the n%26 method because:

ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

We can use (n-1) % 26 instead, then we get a number range from 0 to 25.
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        while n > 0:
            res.append(chr((n - 1) % 26 + ord('A')))
            n = (n - 1) // 26
            
        res.reverse()
        return ''.join(res)