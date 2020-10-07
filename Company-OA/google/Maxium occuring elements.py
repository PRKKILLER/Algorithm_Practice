"""  
Given an array of size N. You are allowed to perform the following operation at most K
times:
In one operation, you can increment an array element by one.

You can perform increment operation on same index more than once. 
You are required to find maximum size subarray of equal elements.

Output:
Return length of the maximum size subarray of equal elements.

Example:
input: arr = [2,4,8,5,9,6], K = 6
output: 3

Explanation:
If chose [8,5,9], we can perform 1 opr on 8, 4 opr on 5, 0 opr on 9. Total opr = 5 < 6
len = 3
"""

"""  
利用 sliding window 和 monotonic queue(单调队列)
monotonic queue用来track sliding window 中最大的元素
对于一个sliding window, total opr = (max_item of window * length of window) - sum
if total opr <= K, window_size++

else if total opr > K, move sliding window start pointer
"""

from collections import deque

def maxEqual(arr, K):
    dq = deque()
    window = 0 # record window size
    start = 0 # recard sliding window's start pointer
    s = 0 # record the sum of the sliding window

    for i, n in enumerate(arr):
        while dq and arr[dq[-1]] <= n:
            dq.pop()

        dq.append(i)
        s += n # sum of the sliding window

        cost = arr[dq[0]] * (window + 1) - s # total number of opr to make the window same

        if cost <= K:
            window += 1
        else:
            # move the start pointer of the sliding window
            while dq[0] <= start:
                dq.popleft()

            # move the start pointer and remove its weight from the sum
            s -= arr[start]
            start += 1

    return window

if __name__ == "__main__":
    arr = [2,4,8,5,9,6]
    print(maxEqual(arr, 6))











