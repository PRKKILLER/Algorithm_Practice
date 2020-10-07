"""  
An e-commerce site tracks the purchases made each day. The product that is purchased the most one day
is the featured product for the following day.
if there is a tie for the prodcut purchased most frequently, those product names are ordered alphabetically
ascending and the last name in the list is chosen

Example:
products = [red,green,red,orange,black,black]
most frequent = [black,red]
since red > black, so the return value is red
"""

from collections import Counter

def solution(products):
    products = sorted(products, reverse=True)
    # most_common返回 n 个最常见元素
    # 计数值相等的元素按首次出现的顺序排序
    # 题目要求当计数值相等时，返回字母顺序最大的一个product
    # 因此先对product排序（逆序），将字母序大的排前
    return Counter(products).most_common(1)[0][0] 

if __name__ == "__main__":
    products = ['red', 'green', 'red', 'orange', 'black', 'black']
    print(solution(products))