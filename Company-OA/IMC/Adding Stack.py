"""  
Implement a stack that accepts the following commands and performs the operations described:

1. push v: push integer v onto the top of the stack
2. pop: pop the top element from the stack
3. inc i v: add v to the bottom i elements in the stack

Additionally, the stack should support the following functions:
1. empty: return true if the stack is empty, false if it is not
2. peek: return the top element on the stack.
3. sum: return the sum of all the elements in the stack.

Example
operations = ['push 4', 'push 5', 'inc 2 1', 'pop', 'pop']
"""

"""  
Share the same ideas as LC-1381. Design a Stack With Increment Operation

Essense: use lazy increment to achieve O(1) increment operation
"""


class CustomStack:
    def __init__(self):
        self.stk = []
        self.add = []
        self.acc = 0

    def push(self, v: int) -> None:
        self.stk.append(v)
        self.add.append(0)
        self.acc += v

    def inc(self, i: int, v: int) -> None:
        if self.add:
            self.add[min(i, len(self.stk)) - 1] += v
            self.acc += v * min(i, len(self.stk))

    def pop(self) -> int:
        if not self.add:
            return -1

        if len(self.add) > 1:
            self.add[-2] += self.add[-1]

        val = self.stk.pop() + self.add.pop()
        self.acc -= val
        return val

    def empty(self) -> bool:
        return len(self.stk) == 0

    def peek(self) -> int:
        if not self.stk:
            return -1

        return self.stk[-1]

    def sum(self) -> int:
        return self.acc


def supperStack(operations: List[str]):
    stk = []
    inc = []
    res = []

    for opr in operations:
        opr = opr.split(' ')
        if opr[0] == 'push':
            val = int(opr[1])
            stk.append(val)
            inc.append(0)
            res.append(val)
            print(val)
        elif opr[0] == 'inc':
            idx, val = int(opr[1]), int(opr[2])
            inc[min(len(stk), idx) - 1] += val
        elif opr[0] == 'pop':
            if len(stk) > 1:
                inc[-2] += inc[-1]
                num = stk.pop() + inc.pop()
                res.append(num)

    return res
