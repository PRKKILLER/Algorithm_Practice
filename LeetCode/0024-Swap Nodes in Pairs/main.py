"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.


Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        tmp = head.next.next
        ret = head.next
        ret.next = head
        head.next = self.swapPairs(tmp)
        return ret

    def swapPairs2(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(-1)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a # point to the second node of the reversed pair

        return dummy.next