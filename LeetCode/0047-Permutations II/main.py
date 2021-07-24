"""  
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.


Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        counter = Counter(nums)
        res = []
        n = len(nums)

        def backtrack(path: List[int]) -> None:
            if len(path) == n:
                res.append(path[:])
                return

            # to avoid duplicates
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    path.append(num)
                    backtrack(path)
                    counter[num] += 1
                    path.pop()

        backtrack([])
        return res
