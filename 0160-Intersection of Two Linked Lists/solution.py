import DataStructure.linked_list.singly_linked_list as slist


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.value = x
#         self.next = None


class Solution(object):
    '''
Write a program to find the node at which the intersection of two singly linked lists begins.

Example:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation:
The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5].
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
    '''
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

def main():
    # test the algorithm
    data = [1, 2, 3, 4, 5]
    L = slist.singly_linked_list()
    L.add_from_list(data)
    L2 = L.head.next.next # L2 point at data "3"
    res = Solution().getIntersectionNode(L.head, L2)
    print(res.data)

if __name__ == "__main__":
    main()



