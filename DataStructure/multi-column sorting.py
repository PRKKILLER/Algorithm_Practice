"""  
多条件排序
"""

"""  
1. 按照元组的第一个从小到大排序
2. 如果第一个相同  则按照元组第2个从大到小 排序
"""

L = [(12, 12), (34, 13), (32, 15), (12, 24), (32, 64), (32, 11)]
L.sort(key=lambda x: (x[0], -x[1]))
print(L)