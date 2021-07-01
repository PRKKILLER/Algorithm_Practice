"""  
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        tmp = [0 for _ in range(m+n)]

        # scan from back to front and store the result in reverse order
        for i in range(m):
            for j in range(n):
                tmp[i+j] += int(num1[m-1-i]) * int(num2[n-1-j])

        # from start to end, do mod and carry, to update to only 1 digit
        carry = 0
        for i in range(len(tmp)):
            num = tmp[i] + carry
            carry, tmp[i] = divmod(num, 10)

        res = []
        for i in range(len(tmp)-1, -1, -1):
            # skip leading zeros
            if not res and tmp[i] == 0:
                continue
            res.append(str(tmp[i]))

        return ''.join(res)
