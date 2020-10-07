"""  
给定一个num, 返回这个数字的每一个digit的乘积：product 和 每一位digit的和：sum 的差值
"""

import functools

def solution(num):
    tmp = [int(d) for d in list(str(num))]

    product = functools.reduce(lambda x, y: x*y, tmp)
    return abs(product - sum(tmp))

print(solution(111))