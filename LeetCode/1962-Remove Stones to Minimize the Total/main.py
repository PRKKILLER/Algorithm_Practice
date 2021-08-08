"""  
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones 
in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).


Example 1:

Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.
"""

"""  
Intiuition: If we want to have the minimum number of stones in the end, we must every time
remove maximum stones from the pile. we can use priority queues to keep track of 
piles with largest stone number
"""




import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = []
        """  
        we push the -num to the heapq to imitate the max heap
        Time complexity: O(klogn)
        """
        for num in piles:
            heapq.heappush(pq, -num)

        for _ in range(k):
            data = -heapq.heappop(pq)
            data -= data // 2
            heapq.heappush(pq, -data)

        return -sum(pq)
