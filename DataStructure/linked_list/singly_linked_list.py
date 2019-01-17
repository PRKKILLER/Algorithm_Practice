from __future__ import print_function

class Node(object): # create a node in the list
    def __init__(self, data):
        self.data = data
        self.next = None

class singly_linked_list(object):
    def __init__(self):
        self.head = None

    def insert_head(self, data): #判断当前head是否为空，若为空，则初始化，若不为空, 更新当前的head
        newNode = Node(data) # create the new node
        if self.head is not None:
            newNode.next = self.head # link new node to the head
        self.head = newNode # make the newNode as the head

    def insert_tail(self, data):
        if self.head is None:
            self.insert_head(data) # call the function to initialize the head
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    def printList(self): # print every item in the linked list
        temp = self.head
        while temp is not None:
            print(temp.data, end='->')
            temp = temp.next
        print()

    def delete_head(self): # delete from the head
        temp = self.head
        if self.head is not None:
            self.head = temp.next
            temp.next = None
        return temp # return deleted head

    def delete_tail(self): # delete from the tail
        temp = self.head
        if self.head is not None:
            if self.head.next is None: # if head is the only node in the linked list
                self.head  = None
            else:
                while temp.next.next is not None:
                    temp =temp.next
                temp.next, temp = None, temp.next
        return temp # return deleted node

    # Remove all elements from a linked list of integers that have value val.
    def delete_elements(self, data):
        dummy = cur = Node(-1)
        dummy.next = self.head # add dummy node to the start of the list
        while cur.next:
            if cur.next.data == data:
                temp = cur.next
                cur.next = temp.next
                temp.next = None
                del temp
            else:
                cur = cur.next
        self.head = dummy.next
        del dummy # delete dummy node after use

    def isEmpty(self):
        return self.head is None

    def reverse(self): # reverse the linked list
        prev = None
        current = self.head

        while current is not None:
            # store current node's next node before current node's pointer reverse
            next_node = current.next
            # reverse the current node's pointer to point at the previous node
            current.next = prev
            # update prev node
            prev = current
            # update current node
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev

    # build the linked list from the data stored in list(built-in structure)
    def add_from_list(self, data):
        if data is None:
            return
        elif not isinstance(data, list):
            self.insert_tail(data)
        else:
            for item in data:
                self.insert_tail(item)

def main():
    # test insert function
    L = singly_linked_list()
    data = [1, 2, 3, 4, 5, 6]
    L.add_from_list(data)
    L.printList()

    # test reverse function
    L.reverse()
    L.printList()


if __name__ == "__main__":
    main()


