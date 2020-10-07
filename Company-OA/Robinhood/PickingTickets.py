"""  
Consider an array of n ticket prices, "tickets". A integer "m" is defined as the size of some subsequence "s",
where each element covers an unbroken range of integers. That is to say, if you were to sort the elements in s,
the absolute difference between any elements j and j+1 would be either 0 or 1.

Determine the maximumm length of a subsequence chosen from the tickets array.

Example:
tickets = [8,5,4,8,4]
valid subsequences sorted are {4,4,5} and {8,8}.
Return 3
"""

from typing import List
from collections import Counter

def solution(arr: List[int]) -> int:
    if len(arr) < 2: return len(arr)

    count = list(dict(Counter(arr)).items())
    count = sorted(count, key=lambda x: x[0])

    memo = set()
    max_len, cur_len= 0, 0

    for item in count:
        memo.add(item[0])
        if item[0] - 1 in memo:
            cur_len += item[1]
            max_len = max(max_len, cur_len)
        else:
            cur_len = item[1]
            max_len = max(max_len, cur_len)

    return max_len


tickets = [8,5,4,8,4]
print(solution(tickets))