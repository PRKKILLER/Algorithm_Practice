"""  
Given a string comprised of lowercase letters, find the length shortest substring that contains
at least one of each of the letters in the string.

E.g.:
givenString = “dabbcabcd”,
all chars appeared in the string: [a,b,c,d]

the shortest substring contains all chars: "abcd", so the answer is 4


Similar to LC-76: https://leetcode.com/problems/minimum-window-substring/
"""


def solution(givenString: str) -> int:
    from collections import defaultdict

    n = len(givenString)

    if n < 2:
        return n

    # count all distinct chars
    dist_cnt = len(set(givenString))
    if dist_cnt == n:
        return n

    dic = defaultdict(int)
    cnt = 0
    start = 0
    min_len = n

    for i in range(n):
        dic[givenString[i]] += 1
        if dic[givenString[i]] == 1:
            cnt += 1

        # if substring contains all chars, try to minimize window by moving left pointer
        if cnt == dist_cnt:
            while dic[givenString[start]] > 1:
                dic[givenString[start]] -= 1
                start += 1

            # update min window length
            min_len = min(min_len, i - start + 1)

    return min_len


print(solution('dabbcabcd'))
