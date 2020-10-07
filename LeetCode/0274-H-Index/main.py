"""  
Given an array of citations (each citation is a non-negative integer) of a researcher, 
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: 
"A scientist has index h if h of his/her N papers have at least h citations each, 
and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.

hIndex的定义：有 h 篇文章的 citation >= h，因此若一个人有 n 篇文章，hIndex <= n
"""

class Solution:
    """  
    该题的主要思路是counting sort
    首先初始化buckets数组，len = n+1
    当citation[i] > n时，将citation[i]放在第n个bucket，其余情况下都放在bucket[cite]中

    因为hIndex是取最大值，因此从后向前遍历buckets数组, 并用cnt记录 >= i 的citation数目
    当cnt >= i，则返回 i
    """
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        for cite in citations:
            if cite > n:
                buckets[n] += 1
            else:
                buckets[cite] += 1
        
        cnt = 0
        for i in range(n, - 1, -1):
            cnt += buckets[i]
            if cnt >= i:
                return i
                
        return 0