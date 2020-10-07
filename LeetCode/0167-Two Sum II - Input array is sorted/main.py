"""  
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

"""  
因为numbers数组是有序的，因此就可以利用双指针，从数组两侧搜索
空间复杂度: O(1)， 时间复杂度: O(n)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            tmp = numbers[i] + numbers[j]
            if tmp < target:
                i += 1
            elif tmp > target:
                j -= 1
            else:
                break
        return [i+1, j+1]