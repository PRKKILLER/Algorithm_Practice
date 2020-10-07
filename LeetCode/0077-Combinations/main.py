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
        self.res = []
        self.backtrack([], n, k, 1)
        return self.res

    def backtrack(self, track, n, k, start):
        # make a copy of the list, so the modification wont affect original list
        track = track[:] 
        if k == 0:
            self.res.append(track)
            return
        
        for i in range(start, n+1):
            track.append(i)
            self.backtrack(track, n, k-1, i+1)
            track.pop()

if __name__ == "__main__":
    sol = Solution()
    res = sol.combine(4, 2)
    print(res)