"""  
Given a string, your task is to count how many distinct palindromic substrings in this string.
"""

def solution(s: str) -> int:
    if not s: return 0

    res = set()
    n = len(s)

    for i in range(n):
        # assume sub-palindrome string's length is odd
        lo, hi = i, i
        while 0 <= lo and hi < n and s[lo] == s[hi]:
            res.add(s[lo:hi+1])
            lo -= 1
            hi += 1

        # assume sub-palindrome string's length is even
        lo, hi = i, i+1
        while 0 <= lo and hi < n and s[lo] == s[hi]:
            res.add(s[lo:hi+1])
            lo -= 1
            hi += 1

    return len(res)

print(solution('aaa'))