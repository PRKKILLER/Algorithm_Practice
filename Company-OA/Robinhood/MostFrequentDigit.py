"""  
返回出现频率最高的数字

Example:
Input: A = [22,2,3,33,5]
Output: [2,3]
"""

from collections import Counter

def solution(arr):
    tmp = []
    for num in arr:
        tmp.extend(list(str(num)))

    counter = list(dict(Counter(tmp)).items())
    counter = sorted(counter, key= lambda x: x[1], reverse=True)
    res = [int(counter[0][0])]
    most_freq = counter[0][1]

    for i in range(1, len(counter)):
        if counter[i][1] == most_freq:
            res.append(int(counter[i][0]))
        else:
            break
    
    return res

A = [22,2,3,33,5]
print(solution(A))