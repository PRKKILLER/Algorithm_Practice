"""  
A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1. 
For example, 321 is a Stepping Number while 421 is not.

Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.


Example 1:

Input: low = 0, high = 21
Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]

Constraints:

0 <= low <= high <= 2 * 10^9
"""


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        """
The idea is to start with all the numbers in [1, 9] and compute new numbers from them and check if they're between low and high. 
For any number n, we can create new numbers by taking the right most digit, 
i.e. mod 10 and check if we can increase the last digit increase 1 or if we can decrease the last digit by 1. 
We can only increase the last digit if the last digit isn't 9. Same for decreasing if the last digit isn't 0. 
The reason we don't include 0 in the initial range is because we would double count for all of 0's children.

Analysis
To analyze the runtime, notice with this method we are essentially doing BFS on a tree with numbers in the range [1, high]. 
The amount of levels the tree has is about log(high) and each node in our tree has 2 children 
(except when least significant digit is 0 or 9). This gives us O(2^(log(n))) runtime if n is high.
        """
        def bfs():
            from collections import deque
            q = deque(range(1, 10))
            while q:
                n = q.popleft()
                if low <= n <= high:
                    res.append(n)
                if n < high:
                    right_most = n % 10
                    n *= 10
                    if right_most > 0:
                        q.append(n + right_most - 1)
                    if right_most < 9:
                        q.append(n + right_most + 1)

        res = []
        if low == 0:
            res.append(0)
        bfs()
        return res
