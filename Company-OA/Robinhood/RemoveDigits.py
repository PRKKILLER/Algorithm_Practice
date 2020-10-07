"""  
给2个字符串a, b
求从字符串'b'中去掉1个数字位后，a < b 的情况（alphanumeric sort）
例如：
a='d1c', b='1b2z'
则b去掉数字位后有2中情况，b1='b2z'，b2='1bz'，让a与这两种情况作比较
"""

def solution(a: str, b: str) -> int:
    if not a or not b: return 0

    res = 0
    n = len(b)
    for i in range(n):
        if i == 0:
            if b[i].isdigit():
                if a < b[1:]:
                    res += 1
        elif i == n - 1:
            if b[i].isdigit():
                if a < b[:-1]:
                    res += 1
        else:
            if b[i].isdigit():
                tmp = b[:i] + b[i+1:]
                if a < tmp:
                    res += 1

    return res

print(solution('d1c', '1b2z'))