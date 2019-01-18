# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    Remove all elements from a linked list of integers that have value val.
    Example:
        Input:  1->2->6->3->4->5->6, val = 6
        Output: 1->2->3->4->5
    '''

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head
        prev = None
        while current:
            if current.data == val and current != head:
                prev.next = current.next
            elif current.data == val and current == head:
                head = current.next
            elif current.data != val:
                prev = current

            current = current.next
        return head


    # 遍历链表，遇到符合条件的值直接跳过。注意要在表头添加dummy node
    def removeElements_v2(self, head ,val):
        """
        :type head: ListNode
        :param val: int
        :rtype: ListNode
        """
        # add dummy node to the start of the list, to ensure always point to the update list.head
        cur = dummy = ListNode(-1)
        dummy.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next # 若当前节点val == val, 跳过该节点
            else:
                cur = cur.next
        return dummy.next

    # 迭代, 一开始先用一个while循环处理head.val == val的情况
    def removeElements_v3(self, head, val):
        """
        :type head: ListNode
        :param val: int
        :rtype: ListNode
        """
        while head and head.val == val: # head.val == val
            head = head.next

        if not head:
            return head

        prev = head
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head



