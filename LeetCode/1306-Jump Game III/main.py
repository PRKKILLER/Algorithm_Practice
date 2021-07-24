"""  
Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index 
with value 0.

Notice that you can not jump outside of the array at any time.


Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
"""


class Solution:
    """  
    标准 BFS 解法，注意在 jump 的时候要保证不能跳出边界
    """

    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import deque

        if arr[start] == 0:
            return True

        n = len(arr)
        dq = deque([start])
        seen = set([start])

        while dq:
            idx = dq.popleft()
            if arr[idx] == 0:
                return True

            l_bound = idx - arr[idx]
            if l_bound >= 0:
                if l_bound not in seen:
                    dq.append(l_bound)
                    seen.add(l_bound)

            r_bound = idx + arr[idx]
            if r_bound < n:
                if r_bound not in seen:
                    dq.append(r_bound)
                    seen.add(r_bound)

        return False
