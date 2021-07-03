"""  
The next greater element of some element x in an array is the first greater element that is 
to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine 
the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""


class Solution:
    """  
    monotonic stack; time complexity: O(M + N)

    Iterate over the nums2 array from the left to right. We push every element nums[i] on the stack 
    if nums2[i] < stack.top(). 
    No entry is made in map for such nums2[i] right now. 
    This happens because the nums2[i] encountered so far are coming in a descending order.

    If we encountered nums2[i] > stack.top(),  then we keep popping the stack until nums2[i] < stack.top()
    And we put every popped element in the stack in the map: M[stack.pop()] = nums2[i]

    Finally, we pop out the remaining elements in the stack, and put theme in the map: M[stack.pop()] = -1
    since the remaining elements have no next greater element

    So we used monotonic stack and hashmap to form (elem: next_greater_elem) map
    """

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, stk = {}, []
        for num in nums2:
            while stk and stk[-1] < num:
                m[stk.pop()] = num

            stk.append(num)

        return [m[num] for m in nums1]
