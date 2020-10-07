"""  
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack:
    """  
    思路：利用两个stack来实现，一个stack用来顺序存放数据，另一个stack用来记录最小值
    min stack难点在于 pop 元素之后怎么更新最小值
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.helper = [] # 用来记录最小值

    def push(self, x: int) -> None:
        self.stk.append(x)
        if not self.helper or x <= self.helper[-1]: # 注意是 <=，不是 < 
            self.helper.append(x)  # 更新最小值

    def pop(self) -> None:
        tmp = self.stk.pop()
        if tmp == self.helper[-1]:
            self.helper.pop()  # 更新最小值

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()