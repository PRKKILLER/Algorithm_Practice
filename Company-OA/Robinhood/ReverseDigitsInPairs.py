"""  
Given an integer n, your task is to reverse its digits in pairs. More formally, if n=d1d2d3...
then the answer should be d2d1d4d3...
if the number of digits is odd, the last digit should stay in the same position.

Example: 
1. n = 123456, return n=214365
2. n = 72328, return n=27238

The second digit of n is not zero
"""

def solution(n: int) -> int:
    num = str(n)
    return int(helper(num))

def helper(num: str):
    num = list(num)
    for i in range(1, len(num), 2):
        num[i-1], num[i] = num[i], num[i-1]

    return ''.join(num)

n = 72328
print(solution(n))