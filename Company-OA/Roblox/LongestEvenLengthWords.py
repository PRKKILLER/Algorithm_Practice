"""  
找一句话里面 最大的偶数长度的单词，如果有多个同样长度的 则返回第一个。
比如说"Time to write great code"，return Time
"""

import re
def solution(s: str) -> str:
    tmp = []
    words = re.split('\W+', s)

    for idx, w in enumerate(words):
        if len(w) % 2 == 0:
            tmp.append((w, idx))
    
    tmp = sorted(tmp, key=lambda x: (len(x[0]), -x[1]), reverse=True)
    return tmp[0][0]


s = 'Time to write great code'
print(solution(s))