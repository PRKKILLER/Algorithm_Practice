"""  
Given an integer array nums and two integers k and t, 
return true if there are two distinct indices i and j in the array such that 
abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""

from typing import List


class Solution:
    """  
    Using Bucket sort to achieve O(N) time complexity.
    We use hashmap to create buckets that covers the range of |0, t|, |t + 1, 2t + 1| (inclusive)...

    For each element x, its bucket label is x // w, where w = t + 1.

    Different from normal bucket sort, we only keep one element in each bucket,
    and if there are two element with differnce <= t, then one of the following will happen:
    1. 2 number in the same bucket
    2. 2 number in neighbor bucket
    """

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0:
            return False

        dic = {}
        w = t + 1

        for idx, num in enumerate(nums):
            bucket_id = num // w
            # check current bucket and its neighbors
            for label in [bucket_id, bucket_id - 1, bucket_id + 1]:
                if label in dic and abs(num - dic[label]) <= t:
                    return True

            # We don't need to store multiple values in a bucket.
            # Because if that is a case, we should return True above.
            # We always update the bucket with the latest (right most) value.
            dic[bucket_id] = num

            # delete bucket that out of the range
            if idx >= k:
                expired = nums[idx - k] // w
                del dic[expired]

        return False
