"""  
You are working with a supplier who is unhappy with the customer IDs a third party site 
generated for them. They are afraid of palindromes, and the list they got from the generator 
is full of them. The supplier wants your help to reduce the number of palindroms that they have to 
work with, while maintaining their carefully formatted order form by keeping the length of the 
customer IDs consent to a new ID if the difference between the new ID and old ID is one letter.
Besides that, the new ID must be alphabetically lower than the old ID.

Design an algorithm that, given an input palindrome ID, returns a new ID that meets the following requires:

1. len(new ID) == len(old ID)
2. new ID is lower alphabetically than the old ID
3. new ID is the lowest value string alphabetically that can be created from the original palindrome after chaning 
exactly one letter

constraint: 1 <= length of oldID <= 1000

Input: oldID

Output: Return a new ID meets all criteria. If it's not possible to create a new to meet all the criteria,
return IMPOSSIBLE.

Example:
input: oldID = 'aaabbaaa'

output: newID = 'aaaabaaa'
"""

def solution(oldID):
    n = len(oldID)
    if n < 2: return 'IMPOSSIBLE'

    mid = n // 2
    oldID = list(oldID)

    for i in range(mid):
        if oldID[i] != 'a':
            oldID[i] = 'a'
            return ''.join(oldID)
    
    return 'IMPOSSIBLE'

test_1 = 'baabaab'
print(solution(test_1))