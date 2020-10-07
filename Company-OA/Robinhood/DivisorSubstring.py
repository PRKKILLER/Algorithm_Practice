"""  
Given 2 integers,n and k. Consider the string representation of n, and find the number of distinct substrings of
length k, such that n is divisible by the number formed by that substring.

Example:
n=120,k=2, return: 2
The divisor substring are 12 and 20 (120 is divisible by both)
"""

def solution(n: int, k: int) -> int:
    n_s = str(n)
    l = len(n_s)
    i = 0
    cnt = 0
    while i + k <= l:
        divisor = int(n_s[i:i+k])
        if divisor == 0:
            i += 1
            continue
        if n % divisor == 0:
            cnt += 1
            i += 1

    return cnt

print(solution(10000,2))