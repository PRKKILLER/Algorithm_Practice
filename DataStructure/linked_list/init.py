# node in the linked_list
class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = Node(value, None)

    def remove(self):
        if self.is_empty:
            return None
        else:
            value = self.head.next
            self.head = self.head.next
            return item

    def empty(self):
        return self.head is None
