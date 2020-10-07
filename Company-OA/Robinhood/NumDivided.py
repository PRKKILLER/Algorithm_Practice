"""  
给一个数, 例如"456"，看这里面有多少个可以被3整除。比如：'4','5','6','45','46','56','456'
"""

def solution(num: str) -> int:
    if not num: return 0

    memo = ['']
    for d in num:
        memo += [item + d for item in memo]
    
    res = 0
    for i in memo[1:]:
        if int(i) % 3 == 0:
            res += 1

    return res

print(solution('456'))
