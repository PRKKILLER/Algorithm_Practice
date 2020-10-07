"""  
给定 1 个list of numbers, 和一个target value
判断list中有几个unique 的 pair加起来和等于 target
"""

def solution(nums, target):
    m = {}
    out = set()

    for i, num in enumerate(nums):
        if target - num in m:
            out.add((num, target - num))
        else:
            m[num] = i
    
    return len(out)

nums = [1,2,1]
target = 3
print(solution(nums, target))