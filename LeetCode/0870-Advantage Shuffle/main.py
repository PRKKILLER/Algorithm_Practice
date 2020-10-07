"""  
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i 
for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.


Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

"""
from collections import deque
from typing import List

class Solution:
    """  
    Greedy approach, 田忌赛马的思想
    """
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        res = [None] * len(A)
        sortedA = sorted(A)
        sortedB = deque(sorted([(b, idx) for idx, b in enumerate(B)]))

        for a in sortedA:
            b, idx = sortedB.popleft()
            # if our current weakest player beat the enemy's weakest player
            if a > b:
                res[idx] = a
            # if our current weakest player failed to beat the enemy, put the enemy back to the front
            # arrange our next weakest player to beat
            else: 
                sortedB.appendleft((b, idx))
                # arrange our current weakest player to beat the enemy's strongest fighter
                last = sortedB.pop()[1]
                res[last] = a
        
        return res


A = [2,7,11,15]
B = [1,10,4,11]
sol = Solution()
print(sol.advantageCount(A, B))