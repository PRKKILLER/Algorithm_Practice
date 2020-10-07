"""  
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """  
    思路：利用hashmap保存节点下标到节点的映射，然后每次让 L_k -> L_n-k
    """
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        
        m = {}
        cur, cnt = head, 0
        while cur:
            m[cnt] = cur
            cur = cur.next
            cnt += 1
        
        dummy = cur = ListNode(-1)
        
        for i in range(cnt//2):
            cur.next = m[i]
            cur = cur.next
            cur.next = None
            
            cur.next = m[cnt-1-i]
            cur = cur.next
            cur.next = None
        
        if cnt % 2:            # 若链表长度为奇数，则将链表最中间的节点append到链表的最后
            cur.next = m[cnt//2]
            cur.next.next = None

    def reorderList2(self, head: ListNode):
        if not head or not head.next or not head.next.next:
            return head
        
        # 1. find the middle of the list, slow 指向链表中点的前一个节点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. reverse the second half
        head2 = self.reverse(slow.next)
        slow.next = None

        # 3. link the two half together
        while head2:
            tmp1 = head.next
            tmp2 = head2.next
            
            head2.next = head.next # head.next是下一个L_k -> L_n-k的起点
            head.next = head2

            head = tmp1
            head2 = tmp2

        
    def reverse(self, head: ListNode):
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev


if __name__ == "__main__":
    sol = Solution()

    l = [1,2,3,4,5]
    head = cur = ListNode(1)
    for num in l[1:]:
        cur.next = ListNode(num)
        cur = cur.next

    sol.reorderList(head)
