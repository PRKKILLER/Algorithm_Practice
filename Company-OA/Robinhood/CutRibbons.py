"""  
Given an array of integers with elements representing lengths of ribbons. 
Your goal is to obtain k ribbons of equal length cutting the ribbons into as many pieces as you want. 
Find the maximum integer length L to obtain at least k ribbons of length L

Example 1:

Input: arr = [1, 2, 3, 4, 9], k = 5
Output: 3
Explanation: cut ribbon of length 9 into 3 pieces of length 3, length 4 into two pieces one of which is length 3 
and the other length 1,
and one piece is already is of length 3. So you get 5 total pieces (satisfying k) and the greatest length L possible 
which would be 3.
"""

def is_valid_cut(ribbon, cur_len, k):
    pieces = 0
    for w in ribbon:
        pieces += w // cur_len
    return True if pieces >= k else False

def solution(ribbon, k):
    max_len = max(ribbon)
    # 最少可以分为1段，最多能够分为 max(ribbon)段(每段长度为1)
    left, right = 1, max_len
    while left + 1 < right:
        mid = (left + right) // 2
        if is_valid_cut(ribbon, mid, k):
            left = mid
        else:
            right = mid - 1
    if is_valid_cut(ribbon, right, k):
        return right
    elif is_valid_cut(ribbon, left, k):
        return left
    else:
        return 0