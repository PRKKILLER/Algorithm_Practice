"""  
Given an array and find the count of a pair number and a single number combination in a row of this array
Target array is a[i - 1], a, a[i + 1]

//Example:
//Input: a = [1, 1, 2, 1, 5, 3, 2, 3]
//Output: 3

//Explain:
//[1, 1, 2] -> two 1 and one 2(O)
//[1, 2, 1] -> two 1 and one 2(O)
//[2, 1, 5] -> one 2, one 1 and one five(X)
//[1, 5, 3] -> (X)
//[5, 3, 2] -> (X)
//[3, 2, 3] -> (O)
"""

def solution(arr):
    if len(arr) < 3: return 0

    pre2 = arr[0]
    pre1 = arr[1]
    res = 0

    for i in range(2, len(arr)):
        if (arr[i] == pre1 and pre1 != pre2) or (arr[i] == pre2 and pre1 != pre2) or (pre1 == pre2 and arr[i] != pre1):
            res += 1
        pre2 = pre1
        pre1 = arr[i]
    
    return res

a = [1, 1, 2, 1, 5, 3, 2, 3]
print(solution(a))