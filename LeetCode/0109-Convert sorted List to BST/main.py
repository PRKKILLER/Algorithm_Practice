"""  
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the 
depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        vals = self.list2arr(head)
        
        # lo, hi represent the start and end of the given array
        def arr2BST(lo, hi):
            if lo > hi: return None
            
            mid = (lo + hi) // 2
            root = TreeNode(vals[mid])
            
            # base case
            if lo == hi: return root
            
            root.left = arr2BST(lo, mid - 1)
            root.right = arr2BST(mid + 1, hi)
            
            return root
        
        return arr2BST(0, len(vals) - 1)


    def list2arr(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        return res