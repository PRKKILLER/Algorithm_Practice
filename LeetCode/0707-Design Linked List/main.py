"""
Design your implementation of the linked list. 
You can choose to use the singly linked list or the doubly linked list
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head: ListNode = None
        self.tail: ListNode = None
        self.length: int = 0

    def __len__(self):
        return self.length

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        tmp = ListNode(val)
        tmp.next = self.head
        self.head = tmp
        self.length += 1

        if self.length == 1:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tmp = ListNode(val)
        self.tail.next = tmp
        self.tail = tmp
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            pre = self.head
            for i in range(index - 1):
                pre = pre.next
            post = pre.next
            cur = ListNode(val)
            pre.next = cur
            cur.next = post
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return 
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            pre = self.head
            for i in range(index - 1):
                pre = pre.next
            
            pre.next = pre.next.next
            if index == self.length - 1:
                self.tail = pre

            self.length -= 1

##################################################################################################

class ListNode2:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head: ListNode2 = None
        self.tail: ListNode2 = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        tmp = ListNode2(val)
        if self.head:
            self.head.prev = tmp
        tmp.next = self.head
        tmp.prev = None
        self.head = tmp
        self.size += 1

        if self.size == 1:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tmp = ListNode2(val)
        if self.tail:
            self.tail.next = tmp
        tmp.prev = self.tail
        tmp.next = None
        self.tail = tmp
        self.size += 1

        if self.size == 1:
            self.head = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.size or index < 0:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            
            pre = cur.prev
            tmp = ListNode2(val)
            tmp.prev = pre
            tmp.next = cur
            pre.next = tmp
            cur.prev = tmp
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.size -= 1
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            
            pre = cur.prev
            post = cur.next
            pre.next = post
            post.prev = pre
            self.size -= 1

###################TEST########################

myList = DoublyLinkedList()
myList.addAtHead(1)
myList.addAtTail(3)
myList.addAtIndex(1, 2)
