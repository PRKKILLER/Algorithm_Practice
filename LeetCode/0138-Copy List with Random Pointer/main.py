""" 
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, 
or null if it does not point to any node.
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # 解法1：保留 old_node -> new_node 的 mapping
    # new_node.random = m[old_node.random]
    def copyRandomList(self, head: Node) -> Node:
        if not head: return None

        new_head = Node(head.val)
        m = {head: new_head}
        p, cur = new_head, head.next
        while cur:
            tmp = Node(cur.val)
            m[cur] = tmp
            p.next = tmp
            p = p.next
            cur = cur.next
        
        p, cur = new_head, head
        while cur:
            if cur.random:
                p.random = m[cur.random]
            p = p.next
            cur = cur.next
        
        return new_head


    # use interwaved list data structure to avoid using mapping
    # Old List: A --> B --> C --> D
    # InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'

    def copyRandomList2(self, head: Node) -> Node:
        if not head: return None

        # create interwaved list
        p = head
        while p:
            tmp = p.next
            p.next = Node(p.val, tmp, None)
            p = tmp
        
        # use interweaved list structure to find the copied list's random pointer
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        
        # isolate copied list from interwaved list structure
        new_head = head.next
        p, cur = new_head, new_head.next
        while cur:
            p.next = cur.next
            p = p.next
            cur = cur.next.next

        return new_head


