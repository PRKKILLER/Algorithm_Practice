"""  
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._new = []
        self._old = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._new.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.shuffle()
        return self._old.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.shuffle()
        return self._old[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._new and not self._old

    def shuffle(self):
        if self._old:
            return

        while self._new:
            self._old.append(self._new.pop())
