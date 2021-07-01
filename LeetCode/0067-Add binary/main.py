"""  
Given two binary strings a and b, return their sum as a binary string.


Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    # bit-by-bit computation
    # space complexity: O(max(M, N))
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        # 向左填充0，让 a,b长度相同，右对齐，方便相加
        if len(a) < n:
            a = a.zfill(n)
        else:
            b = b.zfill(n)

        res = []
        carry = 0

        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry == 0 or carry == 2:
                res.append('0')
            else:
                res.append('1')

            carry //= 2

        if carry:
            res.append('1')

        return ''.join(res[::-1])  # reverse

    # bit manipulation. Add two numbers without using add operator
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        while b:
            ans = a ^ b  # answser without carry
            carry = (a & b) << 1
            a, b = ans, carry

        return bin(a)[2:]
