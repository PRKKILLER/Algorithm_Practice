"""  
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.


Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
"""

"""  
The problem deals with finding number of ways of decoding a string. 
What helps to crack the problem is to think why there would be many ways to decode a string. 
The reason is simple since at any given point we either decode using two digits or single digit. 
This choice while decoding can lead to different combinations.

So this problem can be viewed as as a variant of the classic problem "Climbing stairs"

In the problem "climbing stairs", one can choose to climb one or two stairs at a time,
where in this problem, one can choose to either decode using two digits or single digit
But not as easy as the climbing stairs problem, their are some edge cases and restrictions
in this problem. 
First, for the single digit decode, the digit cannot be '0'
Second, for the two digit decode, the two digit should be in range [10,26]

So, we can than use dynamic programming technique to solve this problem. We use array of DP to 
store the results for subproblems. Specifically, dp[i] is the number of decode ways for substring
of s from index 0 to index i

Algorithm:
1. if string s is empty or contain leading zeros, return 0
2. initialize dp array, dp[0] = 1 to provide the base case
3. start at the index 1, one_digit decode is s[i], two_digit decode is s[i-1:i+1]
4. we then check whether one_digit decode and two_digit is valid.
If the valid two digit decoding is possible then we add dp[i-2] to dp[i].
5. Once we reach the end of the dp array, we would have the number of decode ways to decode string s

Follow up: optimize dp solution, with O(1) space
As we implement the solution, we can notice that dp[i] is only depand on the dp[i-1] and dp[i-2]
Thus, we can easily cut down our O(N) space to O(1) by using only two variables to store the 
last two results.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        # view this problem as the "climbing stairs" alternative

        # if s is empty or string s has leading zeros, return 0
        if not s or s[0] == '0':
            return 0
        
        dp = [0] * len(s)
        dp[0] = 1 
        
        for i in range(1, len(s)):
            one_digit = int(s[i])
            two_digit = int(s[i-1:i+1])
            
            if one_digit != 0:
                dp[i] += dp[i-1]
            
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2] if i >= 2 else 1
            
        return dp[-1]

    def numDecodings2(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        prev_1, prev_2 = 1, 1
        for i in range(1, len(s)):
            cur = 0
            one_digit = int(s[i])
            two_digit = int(s[i-1:i+1])
            
            if one_digit != 0:
                cur += prev_1
            
            if 10 <= two_digit <= 26:
                cur += prev_2
            
            prev_2 = prev_1
            prev_1 = cur
            
        return prev_1