"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        cur, n = head, 0 # n表示list的长度
        while cur:
            n += 1
            cur = cur.next
        
        k = k % n # 对k归一化
        if k == 0:
            return head
        
        cur = head
        # 找到rotate的pivot节点
        for i in range(n - k - 1):
            cur = cur.next
        
        tmp = res = cur.next
        cur.next = None
        while tmp.next:
            tmp = tmp.next
        
        tmp.next = head
        return res


    #  解法2: 遍历整个链表，得到链表的长度n，然后此时将链表的头尾连接
    # 然后再从头出发，向后走 n - k % n 个节点到达新链表头结点的前一个节点，然后再断开链表即可
    def ratateRight2(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        cur, n = head, 1
        while cur.next:
            n += 1
            cur = cur.next
        
        # 头尾节点相连
        cur.next = head
        
        # 对k归一化
        k %= n
        if k == 0:
            return head
        
        # 找到rotate后的链表头结点的前一个节点
        for i in range(n - k):
            cur = cur.next
        
        head = cur.next
        cur.next = None
        return head