"""  
You are given a string that represents time in the format hh:mm. Some of the digits are blank 
(represented by ?). Fill in ? such that the time represented by this string is the maximum possible. 
Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

Example 1:

Input: "?4:5?"
Output: "14:59"
Example 2:

Input: "23:5?"
Output: "23:59"
Example 3:

Input: "2?:22"
Output: "23:22"
"""

def solution(time):
    cTime = list(time)
    ans = list('23:59')

    if cTime[0] == '?':
        ans[0] = '1' if cTime[1] != '?' and cTime[1] > '3' else ans[0]
    else:
        ans[0] = cTime[0]

    if cTime[1] == '?':
        ans[1] = '9' if cTime[0] != '?' and cTime[0] != '2' else ans[1]
    else:
        ans[1] = cTime[1]
    
    ans[3] = ans[3] if cTime[3] == '?' else cTime[3]
    ans[4] = ans[4] if cTime[4] == '?' else cTime[4]

    return ''.join(ans)

if __name__ == "__main__":
    test_1 = '2?:22'
    print(solution(test_1))