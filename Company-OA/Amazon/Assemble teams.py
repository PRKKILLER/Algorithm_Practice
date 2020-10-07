"""  
An Amazon Area Manager is trying to assemble a specialized team from a roster of available
associates. There is a minimum number of associates to be involved, and each associate needs
to have a skill rating within a certain range. Given a list of associates skill levels with desired
upper and lower bounds, determine how many teams can be created from the list

Write an algorithm to find the number of teams that can ev created fulfilling the criteria

Input:
num, an integer representing the number of associates
skills, a list of integers representing the skill levels of associates
skills, a list of integers representign the skill levels of associates
minAssociates, an integer representing the minimum number of team members required
minLevel
maxLevel

Output:
Return an integer representing teh total number of teams that can be formed per the criteria

Constraints:
1 <= num <= 20
1 <= minAssociates <= num
1 <= minLevel <= maxLevel <= 1000
1 <= skills[i] <= 1000

Example:
Input: 
num=6
skills=[12,4,6,13,5,10]
minAssociates=3
minLevel=4
maxLevel=10

Output: 5
"""
from typing import List

def solution(num: int, skills: List[int], minAssociate: int, minLevel: int, maxLevel: int) -> int:
    filtered = [item for item in skills if minLevel <= item <= maxLevel]
    res = 0
    n = len(filtered)
    for i in range(minAssociate, n + 1):
        res += combination(n, i)

    return res

def combination(n, m):
    if n == m: return 1

    m = min(m, n-m)
    res = 1

    for i in range(m):
        res *= (n - i)

    while m:
        res //= m
        m -= 1
    
    return int(res)


num=6
skills=[12,4,6,13,5,10]
minAssociates=3
minLevel=4
maxLevel=10

print(solution(num, skills, minAssociates, minLevel, maxLevel))