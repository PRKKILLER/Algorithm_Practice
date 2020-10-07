"""  
给两个数组，按降序排列输出相同元素的新数组

Example:
a = [700,1340,700,140]
b = [700,1340,1500,700]

return: [1340,700,700]
"""

# 时间复杂度：O(n^2)
def solution(a, b):
    inter = [x for x in a if x in b]
    return sorted(inter, reverse=True)

# 时间复杂度: O(nlogn)
def solution2(a,b):
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    i, j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            i += 1
        else:
            j += 1
    
    return res

if __name__ == "__main__":
    a = [700,1340,700,140]
    b = [700,1340,150,700]
    print(solution2(a,b))