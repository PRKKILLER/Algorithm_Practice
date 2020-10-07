"""  
Input:
The input to the function consists of 2 arguments
planConfig, a string representing the floor plan configuration 
displayStr, a string representing the display unit layout

Output:
Return an integer representing the length of the smallest string which divided
both the strings planCongfig and displayStr, if string planConfig is divisible by 
string displayStr. If no such string is possible then return -1

Example:
input:
planConfig='bcdbcdbcdbcd'
displayStr='bcdbcd'

Output: 3

Explanation:
If string 'bcdbcd' is concatenated twice, it can obtain planConfig. The planConfig is divisible
by string displayStr.
Since it passes the first test, look for the smallest string that can be concatenated to create both strings
planConfig and displayStr.

The string 'bcd' is the smallest string that can be concatenated to create both strings.

So the output = len('bcd')=3
"""

def solution(planConfig: str, displayStr: str) -> int:
    n, m = len(planConfig), len(displayStr)
    if n % m != 0:
        return -1
    if displayStr * (n // m) != planConfig:
        return -1
    
    for i in range(1, m//2 + 1):
        if m % i == 0 and displayStr[:i] * (m//i) == displayStr:
            return i
    
    return len(displayStr)

planConfig='bcdbcdbcdbcd'
displayStr='bcdbcd'
print(solution(planConfig, displayStr))
