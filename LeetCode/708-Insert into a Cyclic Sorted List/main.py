"""
Given a node from a Circular Linked List which is sorted in ascending order, 
write a function to insert a value insertVal into the list such that it remains a sorted circular list. 
The given node(head) can be a reference to any single node in the list, 
and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, 
you may choose any place to insert the new value. After the insertion, 
the circular list should remain sorted.

If the list is empty (i.e., given node is null), 
you should create a new single circular list and return the reference to that single node. 
Otherwise, you should return the original given node.

Example 2:

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). 
We create a new single circular list and return the reference to that single node.
Example 3:

Input: head = [1], insertVal = 0
Output: [1,0]
"""
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def insert(self, head: ListNode, insertVal: int):
        if not head:
            head = ListNode(insertVal)
            head.next = head
            return head
        
        prev, cur = head, head.next
        while cur != head:
            if prev.val <= insertVal <= cur.val:
                break
            # 处理 corner cases:
            # 当prev.val > cur.val时，prev指向的是list中的最大值, cur指向的是list中的最小值
            # 当insertVal >= max 或 insertVal <= min 时，都是插入到最大值节点最后，最小值节点之前
            # 因此这两种情况可以合并处理
            if prev.val > cur.val and (insertVal >= prev.val or insertVal <= cur.val):
                break
            
            prev = cur
            cur = cur.next
        
        prev.next = ListNode(insertVal, cur)
        return head