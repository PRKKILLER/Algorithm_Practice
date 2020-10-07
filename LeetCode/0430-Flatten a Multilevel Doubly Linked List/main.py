"""
You are given a doubly linked list which in addition to the next and previous pointers, 
it could have a child pointer, which may or may not point to a separate doubly linked list. 
These child lists may have one or more children of their own, and so on, 
to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, 
doubly linked list. You are given the head of the first level of the list.

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level 
to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
"""


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    # 思路：
    # 1. start from the head, move one step each time to the next node
    # 当 p.child == None, p = p.next
    # 2. 当 p 有child节点，则转向child chain，一直遍历到child chain的end，将child chain的tail node
    # 链接回到原本的p.next
    # 通过这样做，我们就将child chain merge back to the main thread
    # 然后返回到p，继续move，当找到了有child节点的node，重复上述步骤，直到终点
    def flatten(self, head: Node) -> Node:
        if not head:
            return head
        
        p = head
        while p:
            if not p.child:
                p = p.next
            else:
                tmp = p.child
                # find the tail of the child chain
                while tmp.next:
                    tmp = tmp.next
                # connect tail node to teh p.next
                tmp.next = p.next
                if p.next:
                    p.next.prev = tmp
                # connect p.next with child chain, and remove p.child
                # to merge child chain back to the main thread
                p.next = p.child
                p.child.prev = p
                p.child = None
                p = p.next
        
        return head 

    # 思路：利用stack进行DFS
    def flatten2(self, head: Node) -> Node:
        if not head:
            return head
        
        stk = [head]
        pre = Node(-1)
        while stk:
            root = stk.pop()
            root.prev = pre
            pre.next = root
            pre = root

            if root.next:
                stk.append(root.next)

            if root.child:
                stk.append(root.child)
                root.child = None
        
        head.prev = None
        return head

    # 思路：递归进行DFS
    def flatten3(self, head: Node) -> Node:
        cur = head
        self.dfs(cur)
        return head

    def dfs(self, cur: Node):
        prev = cur
        while cur:
            prev = cur
            if not cur.child:
                cur = cur.next
                continue
            # deal with node with child
            tmp = cur.next # save the original cur's next node, will be used, when back track
            cur.next = cur.child
            cur.child.prev = cur

            # recurse over the child node
            ret = self.dfs(cur.child) # ret is childtail
            cur.child = None
            
            if tmp:
                ret.next = tmp
                tmp.prev = ret
                cur = tmp
            else:
                cur = ret
        
        return prev