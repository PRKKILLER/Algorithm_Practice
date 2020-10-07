"""  
compare 2个string, 只有小写字母。并且：
1. 每个string内部可以任意换位置
2. string中两个letter出现的频率也可以互换
所以： 只要两个string每个frequency出现的次数一样就可以

Example:
'babzccc' 和 'bbazzcz'，就返回true。因为z和c之间可以互换频率。
但是'babzcccm'和'bbazzczi'就不可以，因为'm'只在第1个string中
出现过，'i'只在第2个string中出现过
"""

def solution(a: str, b: str) -> bool:
    if len(a) != len(b): return False

    char_set = set()
    for c in a:
        char_set.add(c)
    
    for c in b:
        if c not in char_set:
            return False

    letter1 = [0] * 26
    letter2 = [0] * 26

    for i in range(len(a)):
        letter1[ord(a[i]) - 97] += 1
        letter2[ord(b[i]) - 97] += 1

    # 横坐标是出现的频率，freq[i]的值是出现频率为i的字符的个数
    freq1 = [0] * len(a)
    freq2 = [0] * len(b)

    for i in range(26):
        if letter1[i]:
            freq1[letter1[i]] += 1
        
        if letter2[i]:
            freq2[letter2[i]] += 1

    for i in range(len(a)):
        if freq1[i] != freq2[i]:
            return False

    return True


a, b = 'babzccc', 'bbazzcz'
print(solution(a, b))