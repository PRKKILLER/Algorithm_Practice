
"""
Given a singly linked list, determine if it is a palindrome.
Example:

Input: 1->2->2->1
Output: true

Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 思路：利用快慢指针找到链表的中点，然后将后半部分链表逆序
    # 比较前半部分链表和后半部分逆序链表是否相等
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 对后半部分列表进行逆序,此时slow是后半部分链表的头结点
        cur, prev = slow, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        head_last = prev # 后半段逆序链表的头结点
        slow = head
        while head_last:
            if head_last.val != slow.val:
                return False
            slow = slow.next
            head_last = head_last.next
        
        return True