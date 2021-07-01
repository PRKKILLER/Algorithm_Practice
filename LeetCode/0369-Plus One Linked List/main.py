"""  
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.

Example 1:

Input: head = [1,2,3]
Output: [1,2,4]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # the optimized solution; space complexity: O(1)
    def plusOne(self, head: ListNode) -> ListNode:
        # sentinel head + textbook addtion
        # find the right most digit not equal to 9, add 1 to it
        # and set all following nines to zero
        sentinel = ListNode(0)
        cur = sentinel.next = head
        not_nine = sentinel

        # find the right most digit not equal to 9
        while cur:
            if cur.val != 9:
                not_nine = cur
            cur = cur.next

        not_nine.val += 1
        cur = not_nine.next

        # set all the following digits to 0
        while cur:
            cur.val = 0
            cur = cur.next

        return sentinel if sentinel.val == 1 else head

# ----------------------------------------------------------------

    # not optimized solution, need O(N) space
    def plusOne2(self, head: ListNode) -> ListNode:
        if not head.next and head.val == 0:
            head.val = 1
            return head

        tmp = []
        cur = head
        l = 0
        while cur:
            tmp.append(cur.val)
            cur = cur.next
            l += 1

        self._plusOne(tmp)
        cur, p = head, 0
        if len(tmp) > l:
            old_head = head
            head = ListNode(1)
            head.next = old_head
            cur, p = old_head, 1

        while p < len(tmp):
            cur.val = tmp[p]
            p += 1
            cur = cur.next

        return head

    def _plusOne(self, arr: List[int]) -> None:
        carry = 0
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 9:
                carry, arr[i] = 1, 0
            else:
                carry, arr[i] = 0, arr[i] + 1
                break

        if carry:
            arr.insert(0, 1)
