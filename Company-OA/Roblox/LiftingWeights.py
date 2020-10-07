"""  
Given an array of weights and a limit, find the maximum weights that the one can choose from array

Example:
arr=[1,3,5], limit = 7
return: 6  since 1+5=6, which can be the maimum weights choose from the array
"""

def subsets(nums):
        res = [[]]
        for num in sorted(nums):
            tmp = [item+[num] for item in res]
            res += tmp
        return res

def solution(arr, limit):
    arr = sorted(arr)
    if limit < arr[0]:
        return 0

    res = 0
    memo = [[]]

    for num in arr:
        flag = True
        copy_memo = memo[:]
        for item in copy_memo:
            cur = [num] + item
            memo += [cur]
            if flag:
                tmp = sum(cur)
                if tmp < limit:
                    res = max(res, tmp)
                elif tmp == limit:
                    return limit
                else:
                    flag = False

    return res


arr=[7,10,19,37,30,11,35,16]
limit = 49
print(solution(arr, limit))