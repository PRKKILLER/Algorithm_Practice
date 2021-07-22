"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n: int, k: int):
        def backtrack(start: int, path: List[int], sz: int) -> None:
            if sz == k:
                res.append(path)
                return

            for num in range(start, n + 1):
                # make decisions
                path.append(num)
                # move to next state
                # it is important to do "path[:]" here to make a copy
                backtrack(num + 1, path[:], sz + 1)
                # backtrack
                path.pop()

        res = []
        backtrack(1, [], 0)
        return res
