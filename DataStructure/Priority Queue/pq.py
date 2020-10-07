import heapq
import functools
 
# Abstract & Encapsulate
class PriorityQueue:
    def __init__(self, cmp = lambda x, y: x > y):
        self.container = []
        self.getKey = functools.cmp_to_key(
            lambda x, y: -1 if cmp(x, y) else 1 if cmp(y, x) else 0)
 
    def push(self, item):
        heapq.heappush(self.container, (self.getKey(item), item))
 
    def pop(self):
        return heapq.heappop(self.container)[1]
 
 
# 使用样例 1
# ------------------------------------------------------------------------------
pq = PriorityQueue()
 
pq.push(1)
pq.push(2)
pq.push(3)
 
print(pq.pop())
print(pq.pop())
print(pq.pop())
 
# 输出：
# 3
# 2
# 1
 
 
# 使用样例 2
# ------------------------------------------------------------------------------
pq = PriorityQueue(lambda x, y: x[0] < y[0])
 
pq.push((4, 3))
pq.push((3, 2))
pq.push((2, 1))
 
print(pq.pop())
print(pq.pop())
print(pq.pop())
 
# 输出：
# (2, 1)
# (3, 2)
# (4, 3)
 
 
# 使用样例 3
# ------------------------------------------------------------------------------
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return str(self.__dict__)
 
pq = PriorityQueue(lambda l, r: l.y > r.y if l.x == r.x else l.x < r.x)
 
pq.push(Point(1, 2, 3))
pq.push(Point(4, 3, 2))
pq.push(Point(4, 5, 6))
 
print(pq.pop())
print(pq.pop())
print(pq.pop())
 
# 输出：
# {'x': 1, 'y': 2, 'z': 3}
# {'x': 4, 'y': 5, 'z': 6}
# {'x': 4, 'y': 3, 'z': 2}