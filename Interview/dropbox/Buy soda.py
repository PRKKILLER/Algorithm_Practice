"""  

Given a set of candidate numbers (C) (without duplicates) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
    - All numbers (including target) will be positive integers.
    - The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]

"""

from typing import List
from collections import defaultdict
from copy import deepcopy

"""  
Time complexity: O(NlogN) + O(NT)  ??
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        uniqueComboSum = defaultdict(set)
        uniqueComboSum[0].add(())

        for num in sorted(candidates):
            for cur_sum, combos in deepcopy(uniqueComboSum).items():
                new_sum = cur_sum + num

                if new_sum <= target:
                    for combo in combos:
                        uniqueComboSum[new_sum].add(combo + (num,))

        return [list(combo) for combo in uniqueComboSum[target]]