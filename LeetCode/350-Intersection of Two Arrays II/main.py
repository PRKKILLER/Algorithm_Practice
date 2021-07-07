"""  
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and 
you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""


class Solution:
    # time complexity: O(M + N)
    # space complexity: O(M + N)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        from collections import Counter

        c1, c2 = Counter(nums1), Counter(nums2)
        res = []

        for num in c1:
            if num in c2:
                cnt = min(c1[num], c2[num])
                res += [num] * cnt

        return res

    # only store the counter of samller size array
    # space complexity: O(min(M, N))

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        from collections import Counter
        # do the counter for the smaller array
        m = Counter(nums1)

        # store the intersection of 2 arrays in the longer array
        # so we don't need to allocate extra space for the result
        p = 0
        for num in nums2:
            if num in m and m[num] > 0:
                m[num] -= 1
                nums2[p] = num
                p += 1

        return nums2[:p]
