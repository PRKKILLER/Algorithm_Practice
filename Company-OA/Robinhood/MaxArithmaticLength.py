"""  

"""

from math import gcd

def solution(a, b):
    factorsOfDifference = set()

    if (len(a) > 1):
        num = a[1] - a[0]
        for i in range(2, len(a)):
            num = gcd(num, a[i] - a[i-1])
            
    
    for i in range(1, num+1):
        if num % i == 0:
            factorsOfDifference.add(i)
    
    maxLength = -1
    for factor in factorsOfDifference:
        cur = a[0] + factor
        length = 1
        while cur in a or cur in b:
            length += 1
            cur += factor
        if cur >= a[-1]:
            cur = a[0] - factor
            while cur in b:
                cur -= factor
                length += 1
            maxLength = max(maxLength, length)
    
    return maxLength