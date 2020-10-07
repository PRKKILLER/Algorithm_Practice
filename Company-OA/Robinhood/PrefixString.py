"""  
Given string "s", and array of strings "a". "s" is said to a prefix-string of a if it is a concatenation of some prefix
of the array "a". 
i.e. If there exists some index i, such that s = a[0]+a[1]+...+a[i]

For example, for a = ['one','two','three'], strings s='one', s='onetwo' are prefix-strings,
while s='two', s='onetw' and s='onethree' are not

Given 2 array of strins a and b, determine whether all the given strings in b are prefix-strins of a

Example:
a=['one','twothree','four'], b=['one','onetwo'], 
output: false.

The 'onetwo' is not a prefix-string of a, since it doesn't fully match the concatenated elements of a
"""

from typing import List

def solution(a: List[str], b: List[str]) -> bool:
    tmp = [a[0]]
    for i in range(1, len(a)):
        tmp.append(tmp[i-1] + a[i])
    
    tmp = set(tmp)

    for s in b:
        if s not in tmp:
            return False

    return True

a=['one','twothree','four']
b=['one','onetwo']
print(solution(a, b))