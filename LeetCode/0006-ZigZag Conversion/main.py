"""  
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

理解题意：将字符串写成 从上向下排的 'Z' 型
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        if numRows == 1 or numRows > l:
            return s

        rows = [[] for _ in range(l)]
        row_idx, step = 0, 1

        for c in s:
            rows[row_idx].append(c)
            # we only change the direction when we reach the top/bottom of the rows
            if row_idx == 0:
                step = 1
            elif row_idx == l - 1:
                step = -1

            row_idx += step

        return ''.join([''.join(rows) for row in rows])
