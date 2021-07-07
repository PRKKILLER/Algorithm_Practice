class Solution(object):
    '''
Given two arrays, write a function to compute their intersection.
    Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

    Note:

    Each element in the result must be unique.
    The result can be in any order.
    '''

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [i for i in nums1 if i in nums2]
        return list(set(res))

    def intersection_v2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2)
