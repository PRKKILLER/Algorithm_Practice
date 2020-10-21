"""  
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
evict the least recently used key.


Follow up:
Could you do get and put in O(1) time complexity?


Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""


"""  
Approach1: using HashMap and Doubly-Linked List

- Get the key / Check if the key exists

- Put the key

- Delete the first added key

The first two operations in O(1) time are provided by the standard hashmap
and the last one - by linked list

O(1) time are provided by the standard hashmap, and the last one - by linked list.
"""

class DLinkedNode:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        # important
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            new_node = DLinkedNode(key, value)
            self._add_node(new_node)
            self.cache[key] = new_node
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size = self.capacity
        else:
            node.val = value
            self._move_to_head(node)


    def _add_node(self, node: DLinkedNode):
        """  
        always add node to the right side of the head
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedNode):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node: DLinkedNode):
        """  
        move certain node in between to the head
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """  
        pop the last node in the DLinked list
        """
        res = self.tail.prev
        self._remove_node(res)
        return res


"""  
方法2： use Ordered dict

There is a structure called ordered dictionary, it combines behind both hashmap and linked list. 
In Python this structure is called OrderedDict and in Java LinkedHashMap.
"""

from collections import OrderedDict

class LRUCache2(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        # move to head
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)