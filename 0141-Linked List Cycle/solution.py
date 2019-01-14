# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
    '''

    # 思路： 快慢指针，若有环存在，快慢指针会最终相遇.
    # 时间复杂度: O(N)******- 空间复杂度: O(1)
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head # 2 move in one turn
        slow = head # 1 move in one turn

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    # 思路: 用字典存储已遍历过的node
    # 时间复杂度: O(N) ** ** ** - 空间复杂度: O(N)
    def hasCycle_v2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        check = {}
        while head:
            if head in check:
                return True
            check[head] = 1
            head = head.next
        return False
