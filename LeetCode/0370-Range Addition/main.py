"""  
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. 
In the ith operation, you should increment all the elements 
arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.

Example: 
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
"""

from typing import List


class Solution:
    """  
    Use lazy incremental technique to solve this problem can achieve O(N + K) time complexity
    we only store every start index for each inc value;
    and we store "-inc" value for "end+1" index

    We update value at start index because it will be used in the future when we are adding up the values
    for the sum at each index from start to end (both inclusive). 
    We update "negative value" at "end + 1", because the positive value of it should be only added at its previous index
    (the "end index"), since "end + 1" out of the range, so we should distract "inc" value between "start ~ end"
    """

    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length

        for start, end, inc in updates:
            res[start] += inc
            if end < length - 1:
                res[end + 1] -= inc

        for i in range(1, length):
            res[i] += res[i - 1]

        return res
