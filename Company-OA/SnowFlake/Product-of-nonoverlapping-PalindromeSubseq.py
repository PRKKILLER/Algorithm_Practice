"""  
https://leetcode.com/discuss/interview-question/algorithms/202924/ascend-online-assessment-product-of-palindromes


A palindrome is a sequence of characters which reads the same forward and backwards. 
For example: madam and dad are palindromes, but eva and sam are not.
A subsequence is a group of characters chosen from a list while maintaining their order. 
For instance, the subsequences of abc are [a,b,c,ab,ac,bc,abc]
The score of string s is the maximum product of two non-overlapping palindromic subsequences of s 
that we_ll refer to as a and b. In other words, score(s) = max(length(a) x length(b)).
There may be multiple ways to choose a and b, but there can't be any overlap between the two subsequences. 
For example:

Index 0123456
    s attract
Palindromic subsequences are [a,t,r,c,t,aa,tt,ata,ara,ttt,trt,tat,tct,atta]. 
Many of these subsequences overlap, however (e.g. atta and tct) 
The maximum score is obtained using the subsequence atta, |atta| = 4 and |c| or |t| = 1, 4 x 1 = 4.

Constraints
1 < |s| <= 3000
s[i] is of ascii[a-z]

Sample Input
acdapmpomp

Sample Output
15

Explanation
Given s = "acdapmpomp", we can choose a = "aca" and b= "pmpmp" to get a maximal product of score = 3 x 5 = 15.
"""

# original question: LC-516. Longest Palindromic Subsequence


def solution(s: str) -> int:
    size = len(s)
    dp = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        dp[i][i] = 1

    for d in range(1, size):
        for i in range(size - d):
            j = i + d
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    res = 0
    for i in range(size - 1):
        res = max(res, dp[0][i] * dp[i + 1][size - 1])

    return res


s = 'acdapmpomp'
print(solution(s))
