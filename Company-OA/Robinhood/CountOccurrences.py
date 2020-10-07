"""  
You are given an integer n. Your task is to calculate how many times the digits 0, 2, and 4 appear in all the 
non-negative integers up to n(0,1,...,n)

Example: For n = 10, the output should be countOccurrences(n) = 4

The digit 0 appears in numbers 0 and 10 once, for a totle of 2 occurrences
The digit 2 appears in the number 2 once, for a totle of 1 occurence
The digit 4 appears in the number 4 once, for a toal of 1 occurrence
"""

def solution(n):
    tmp = ''.join([str(x) for x in range(n+1)])
    cnt = 0
    for c in tmp:
        c = int(c)
        if c == 0 or c == 2 or c == 4:
            cnt += 1

    return cnt

print(solution(10))