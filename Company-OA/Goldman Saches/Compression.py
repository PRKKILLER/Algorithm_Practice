"""  
Write an algorithm to compress a string

Example: Input = "abaasass"
Output = "aba2sas2"
"""

def solution(s: str) -> str:
    if len(s) < 2:
        return s

    res, cnt = '', 1

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            if cnt == 1:
                res += s[i]
            else:
                res = res + s[i] + str(cnt)
            cnt = 1
    
    if cnt == 1:
        res += s[-1]
    else:
        res = res + s[-1] + str(cnt)
    
    return res

a = "abaasass"
print(solution(a))