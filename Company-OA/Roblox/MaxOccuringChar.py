"""  
Given a string, return the character that appears the maximum number of times in the string.
String will only contain ASCII chars.

If there is a tie in the maximum number of times of char appears in the string, return the character
that appears first in the string.
"""

from collections import Counter

def solution(s: str):
    count = Counter(s)
    return count.most_common(1)

print(solution('abbbaacc'))