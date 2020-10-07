"""  
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return head

        pre, cur = None, head
        cnt = 0
        while cur:
            cnt += 1
            if cnt == k:
                break
            cur = cur.next
        
        if cnt < k:    # 若以head开头的list长度 < k，则直接返回head
            return head
        
        cur = head
        while cnt > 0:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            cnt -= 1
        
        new_head = pre
        head.next = self.reverseKGroup(cur, k)
        return new_head
