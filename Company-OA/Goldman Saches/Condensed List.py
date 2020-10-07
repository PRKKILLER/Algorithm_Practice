"""  
Given a list of integers, remove any nodes that have values that have previously occurred in the list
and return a reference to the head of the list

Example:
Input: 3 -> 4 -> 3 -> 6
Output: 3 -> 4 -> 3
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def solution(head: ListNode):
    if not head: return head

    dummy = cur = ListNode(-1)
    dummy.next = head
    s = set()

    while cur.next:
        if not cur.next.val in s:
            s.add(cur.next.val)
        else:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = None
        cur = cur.next

    return head

head = ListNode(3)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(6)

res = solution(head)
while res:
    print(res.val, end="  ")
    res = res.next

