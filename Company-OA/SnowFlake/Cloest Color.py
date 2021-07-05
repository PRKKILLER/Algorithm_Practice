"""  
reference RGB value:

black: (0,0,0); white: (255,255,255)
red: (255,0,0); green: (0,255,0); blue: (0,0,255)

Input:
string pixels[n]: an array of 24-bit binary strings represents pixels

e.g.: [000000001111111100000110] represents RGB value as (0, 255,6)

Calculate its euclidian distance to each reference color, and find the closest color

Output: 
string[n]: each element i  represents the coloest color for its associated pixel i

"""
from functools import reduce
from typing import List


def solution(pixels: List[str]) -> List[str]:
    m = {(0, 0, 0): 'Black', (255, 255, 255): 'White',
         (255, 0, 0): 'Red', (0, 255, 0): 'Green', (0, 0, 255): 'Blue'}

    def calcShortestDistance(color):
        dis = float('inf')
        ret = ''
        for c in m:
            s = sum([abs(x[0] - x[1]) for x in zip(color, c)])
            if s < dis:
                dis = s
                ret = m[c]

        return ret

    res = []
    for p in pixels:
        color = (int(p[:8], 2), int(p[8:16], 2), int(p[16:], 2))
        res.append(calcShortestDistance(color))

    return res


p = ['000000001111111100000110']
print(solution(p))
