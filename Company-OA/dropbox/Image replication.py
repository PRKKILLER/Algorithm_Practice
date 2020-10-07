"""  
We have n databases in an array a, where a[i] is the file size limit of that database. 
We want to put a image in a database but we also want to copy the image over to the next k-1 databases 
adjacent to this one. Therefore the file size is limited by the k databases we choose. 
Find the maximum file size we can put. Example:

arr = [1, 6, 3, 2, 1] and k = 3 
Our options are: [1,6,3], [6,3,2], [3,2,1]. 
Each of these options can store files of size at most 1, 2, 1 respectively 
because min([1,6,3]), min([6,3,2]), and min([3,2,1]) = 1, 2, 1 respectively. 
Therefore, the maximum file we can store in this array of databases is 2 because max(1, 2, 1) = 2.
"""

# This solution will result in TLE
def solution(servers, k):
    if k == 1: return max(servers)

    maxImg = 0
    lo, hi = 0, k-1
    while hi < len(servers):
        maxImg = max(maxImg, min(servers[lo:hi+1]))
        lo += 1
        hi += 1
    
    return maxImg

from collections import deque

def minSlidingWindow(servers, k):
    d = deque()
    res = []

    for i, n in enumerate(servers):
        # delete the indices whose value is greater than n
        while d and servers[d[-1]] >= n:
            d.pop()

        d.append(i)

        # make sure the leftmost indice is in-bound
        while d[0] <= i - k:
            d.popleft()
        
        if i + 1 >= k:
            res.append(servers[d[0]])

    return max(res)


if __name__ == "__main__":
    arr, k = [2,5,4,6,8], 3
    print(minSlidingWindow(arr, k))
