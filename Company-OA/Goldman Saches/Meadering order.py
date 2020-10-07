"""  
An array sorted in meandering order is: [first_largest, first_smallest, second_largest, second_smallest]
Write an algorithm to sort the array in meadering order
"""

from typing import List

def solution(nums: List[int]) -> List[int]:
    descend = sorted(nums, reverse=True)
    ascend = sorted(nums)
    res = []

    for i in range(len(nums)):
        if i % 2 == 0:
            res.append(descend[i//2])
        else:
            res.append(ascend[i//2])
    
    return res