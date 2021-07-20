"""  
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""

from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = Counter(nums).most_common(k)  # [(num, freq)...]
        return [elem[0] for elem in topK]

    # 利用bucket sort
    """  
    freq_map保存 num -> 出现次数 的映射
    bucket是List[List], bucket的下标对应的是frequency
    bucket[i]保存了frequency=i的所有数字

    Time complexity: O(N)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # index represents the frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        num_freq = Counter(nums).items()

        for num, freq in num_freq:
            buckets[freq].append(num)

        res = []
        for item in buckets[::-1]:
            if item:
                for num in item:
                    res.append(num)
                    if len(res) == k:
                        return res

        return res
