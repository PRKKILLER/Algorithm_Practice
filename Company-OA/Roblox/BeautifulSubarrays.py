"""  
A beautiful subarray is defined as an array of any length having a specific number of odd element. Given an array
of integers and a number of odd elements that constitutes beauty, create as many distinct beautiful subarrays as 
possible. Distinct means the arrays don't share identical starting and ending indices, though they may share of the
two.

For example:
input: array=[1,2,3,4,5], k=2
output: 4
[1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5]
"""

def solution(arr, k):
    n = len(arr)
    cnt = 0

    prefix = [0] * n
    odd = 0

    for i in range(n):
        prefix[odd] += 1

        if arr[i] % 2:
            odd += 1
        
        if odd >= k:
            cnt += prefix[odd - k]
    
    return cnt

array=[1,2,3,4,5]
k=2
print(solution(array, k))