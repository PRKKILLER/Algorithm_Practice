"""  
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), 
where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
"""

"""  
Count the elements with Counter
If k > 0, for each element i, check if i + k exist.
If k == 0, for each element i, check if count[i] > 1
"""


class Solution:
    # Time complexity: O(N)
    # space complexity: O(N)
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter

        c = Counter(nums)  # {element: frequency}
        cnt = 0

        if k > 0:
            for i in c:
                if i + k in c:
                    cnt += 1
        elif k == 0:
            for i in c:
                if c[i] > 1:
                    cnt += 1

        return cnt

    # time complexity: O(NlogN)
    # space complexity: O(1)
    def findPairs2(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        res = 0
        lo, hi, size = 0, 1, len(nums)

        while hi < size:
            diff = nums[hi] - nums[lo]
            if diff == k:
                res += 1
                lo, hi = lo + 1, hi + 1
                while lo < size and nums[lo] == nums[lo - 1]:
                    lo += 1
                while hi < size and nums[hi] == nums[hi - 1]:
                    hi += 1
            elif diff < k:
                hi += 1
            else:
                lo += 1

            if lo == hi:
                hi += 1

        return res
