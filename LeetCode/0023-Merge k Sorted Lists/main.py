"""  
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        
        n = len(lists)
        while n > 1:
            k = (n + 1) // 2
            for i in range(n // 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[k+i])
            
            n = k
        
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        head = l1 if l1.val <= l2.val else l2
        not_head = l1 if l1.val > l2.val else l2
        
        head.next = self.mergeTwoLists(head.next, not_head)
        
        return head