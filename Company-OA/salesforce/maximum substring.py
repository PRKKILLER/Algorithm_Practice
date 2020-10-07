"""  
A substring is a contiguous sequence of characters whithin a string Given a string,
determine the alphabetically maximus substring

Example:
s="baca"
unique substrings: [b,ba,bac,baca,a,ac,aca,c,ca,a]
Arraging the substring alphabetically: [a,ac,aca,b,ba,bac,baca,c,ca]
return: 'ca'
"""

def solution(s):
    if not s: return s

    tmp = [0, s[0]]

    for i, c in enumerate(s):
        if c > tmp[1]:
            tmp[0] = i
            tmp[1] = c

    return s[tmp[0]:]

if __name__ == "__main__":
    s="baca"
    print(solution(s)) 