"""  
Given an int array nums and an int target, find how many unique pairs in the array 
such that their sum is equal to target. Return the number of pairs.

Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47

注意：nums 并不是 sorted array
"""


def solution(nums: List[int], target: int) -> int:
    res, lookup = set(), set()

    for num in nums:
        t = target - num
        if t in lookup:
            tup = (num, t) if num < t else (t, num)
            if tup not in res:
                res.add(tup)
        lookup.add(num)

    return len(res)
