# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    Reverse the singly linked list
    '''

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head = prev
        return head

    # 头插法
    def reverseList2(self, head):
        if not head: return

        dummy = ListNode(-1)
        dummy.next = cur = head
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            dummy.next = tmp
        
        return dummy.next

    def reverseList3(self, head):
        if not head or not head.next:
            return head

        node_last = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return node_last