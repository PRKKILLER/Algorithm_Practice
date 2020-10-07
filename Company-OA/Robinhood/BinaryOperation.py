"""  
https://leetcode.com/discuss/interview-question/788264/Robinhood-or-OA-New-Grad
"""

def binary(n,operations):
    s=[0]*n
    m=0
    for op in  operations:
        if op=="L":
            if m<n:
                s[m]=1
                while m<n and s[m]:
                    m+=1
        else:
            ind=int(op[1:])
            s[ind]=0
            m=min(m,ind)
    return ''.join(str(i) for i in s)
    
n=10
operations=["L","L","C0","L","C3"]
print(binary(n,operations))