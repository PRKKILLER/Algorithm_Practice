"""
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity 
and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList2(self, head):
        if not head or not head.next:
            return head

        odd, even = head, head.next
        evenHead = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = evenHead
        return head


    # 解法1：分别取出odd, even节点，然后重新拼接
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd, even = ListNode(-1), ListNode(0)
        curEven = even

        cur, idx = head, 1
        while cur:
            if idx % 2:
                odd.next = cur
                odd = odd.next
            else:
                curEven.next = cur
                curEven = curEven.next
            idx += 1
            cur = cur.next
        
        # 当list长度为奇数时（出循环时，idx是偶数），要将最后一个偶数项的next=None
        # 避免城环
        if idx % 2 == 0:
            curEven.next = None
        
        odd.next = even.next
        return head