"""  
Given a positive integer n, find the smallest integer which has exactly the same digits 
existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer 
but it does not fit in 32-bit integer, return -1.


Example 1:

Input: n = 12
Output: 21

Note: This question is equivalent to the famous question: 0031-Nextpermutation
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(str(n))

        # Note: the last permutation of given digits is the number that digits being arranged in descending order
        pivot = -1

        # 1. Start from the right to left, find the first digit which is not in ascending order
        for i in range(len(num) - 1, 0, -1):
            if num[i - 1] < num[i]:
                pivot = i - 1
                break

        # if the pivot is -1, which means the current number is the last permutation
        if pivot == -1:
            return -1

        # 2. Start from the right to left, find the rightmost digit that is greater than num[pivot]
        # do the swap
        for i in range(len(num) - 1, pivot, -1):
            if num[i] > num[pivot]:
                num[pivot], num[i] = num[i], num[pivot]
                break

        # 3. Now, the digits on the right side of the pivot is in descending order
        # since we need the smallest greater number, we need to reverse the digits
        num = num[:pivot + 1] + num[-1:pivot:-1]

        res = int(''.join(num))
        return res if res <= 2**31 - 1 else -1
