"""  
Given string s, consider the following algorithm applied to this string:

1. Take all the prefixes of the string, and choose the longest palindrome between them
2. If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step
with the updated string. Otherwise, end the algorithm with current string s as a result.

Implement above algorithm and return its result when applied to string s
"""

def solution(s: str):
    if len(s) < 2: return s

    while True:
        max_palindrome = LongestPalindromicPrefix(s)
        n = len(max_palindrome)
        if n < 2:
            break
        else:
            s = s[n:]

    return s



# Function to find the longest prefix  
# which is palindromic  
def LongestPalindromicPrefix(Str): 

    # Create temporary string 
    temp = Str + "?"

    # Reverse the string Str 
    Str = Str[::-1] 

    # Append string Str to temp 
    temp = temp + Str

    # Find the length of string temp 
    n = len(temp) 

    # lps[] array for string temp 
    lps = [0] * n 

    # Iterate the string temp 
    for i in range(1, n): 

        # Length of longest prefix  
        # till less than i 
        Len = lps[i - 1] 

        # Calculate length for i+1 
        while (Len > 0 and temp[Len] != temp[i]): 
            Len = lps[Len - 1] 

        # If character at currrent index 
        # Len are same then increment 
        # length by 1 
        if (temp[i] == temp[Len]): 
            Len += 1

        # Update the length at current 
        # index to Len 
        lps[i] = Len

    # return the palindromic string of max_len 
    return temp[0 : lps[n - 1]] 


print(solution('aaacodedoc'))