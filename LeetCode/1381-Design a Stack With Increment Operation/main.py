"""  
Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize): 

1. Initializes the object with maxSize which is the maximum number of elements in the stack or 
do nothing if the stack reached the maxSize.

2. void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.

3. int pop() Pops and returns the top of stack or -1 if the stack is empty.

4. void inc(int k, int val) Increments the bottom k elements of the stack by val. 
If there are less than k elements in the stack, just increment all the elements in the stack.
"""

""" 
Best explanation: 
https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/843182/lee215's-solution-with-more-explanation


The tricky part of this problem is to come up a solution to do inc operation with O(1) time complexity
The idea here is to do "lazy increment"

We can use an additional array to record the increment value
inc[i] means the increment value for all elements between stack[0] ~ stack[i]

The most important property for the inc array is that only inc[-1] (the last element) accurately encodes what to
implement by. And we need to keep "inc array" has the same size as "stack".

When we do pop operation, we also need to pop the inc array. However, since inc[i] denotes the increment value
for all elements between 0 ~ i, so when we pop out the last element of the inc array, 
we need to keep track this incremental value, which can be done by: inc[-2] += inc[-1]
"""


class CustomStack:
    def __init__(self, maxSize: int):
        self.sz = maxSize
        self.stk = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stk) < self.sz:
            self.stk.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stk:
            return -1

        if len(self.stk) > 1:
            self.inc[-2] += self.inc[-1]

        return self.stk.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val
