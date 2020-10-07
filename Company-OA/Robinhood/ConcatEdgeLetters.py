"""  
Construct a 2-character string, where the ith element is equal to the fist character of a[i], concatenated with the last
character of a[i+1]

For the final element, concatmate the first character of a[a.length-1] with the last character of a[0]
"""

from typing import List

def solution(arr: List[str]) -> List[str]:
    n = len(arr)
    arr += [arr[0]]
    res = []
    for i in range(n):
        res.append(arr[i][0] + arr[i+1][-1])

    return res

a = ['cat', 'dog', 'ferret', 'scorpion']
print(solution(a))