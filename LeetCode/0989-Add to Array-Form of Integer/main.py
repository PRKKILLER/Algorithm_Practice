"""  
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.


Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 4:

Input: num = [9,9,9,9,9,9,9,9,9,9], k = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000

Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104
"""


class Solution:
    # take k it self as a carry
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        idx = len(num) - 1
        while idx >= 0 and k > 0:
            k, num[idx] = divmod(num[idx] + k, 10)
            idx -= 1

        while k > 0:
            num.insert(0, k % 10)
            k //= 10

        return num
