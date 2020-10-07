"""  
Given an array arr[] consisting of non-negative integers, the task is to find the number of ways to split the array 
into three non-empty contiguous subarrays such that their respective sum of elements are in increasing order.

Example:

Input: arr[] = {2, 3, 1, 7} 
Output: 2 
Explanation: 
{{2}, {3, 1}, {7}}, {{2}, {3}, {1, 7}} are the possible splits.

Input: arr[] = {1, 2, 0} 
Output: 0

"""
from typing import List

def solution(arr: List[int]) -> int:
    cnt, n = 0, len(arr)
    prefix_sum = [0] * n
    suffix_sum = [0] * n

    # construct prefix sum array
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    # construct suffix sum array
    suffix_sum[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix_sum[i] = arr[i] + suffix_sum[i+1]

    curr_subarr_sum = 0
    lo = hi = 1
    old_hi, old_curr_subarr_sum= 0, 0

    while hi < n - 1 and lo <= hi:
        # updating curr_subarr_sum while curr_subarr_sum < prefix_sum[lo-1]
        while hi < n - 1 and curr_subarr_sum < prefix_sum[lo-1]:
            curr_subarr_sum += arr[hi]
            hi += 1

        if curr_subarr_sum < prefix_sum[lo-1]:
            break

        old_hi = hi
        old_curr_subarr_sum = curr_subarr_sum

        # updating curr_subarr_sum while curr_subarr_sum <= suffix_sum[hi]
        if curr_subarr_sum <= suffix_sum[hi]:
            cnt += 1
        
            curr_subarr_sum += arr[hi]
            while hi < n - 1 and curr_subarr_sum <= suffix_sum[hi+1]:
                cnt += 1
                hi += 1
                curr_subarr_sum += arr[hi]
        
        curr_subarr_sum = old_curr_subarr_sum - arr[lo]
        lo += 1
        hi = old_hi

    return cnt

arr = [ 1,1,1 ] 
print(solution(arr))

