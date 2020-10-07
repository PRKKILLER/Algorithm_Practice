"""  
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. 
If you find more than one maximum elements, only remove the top-most one.

Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

"""

"""  
该题的难点在于 popMax() 后，peekMax() 的准确性
利用 pair 数据结构：(element, largest element so far)
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []  
    
    def push(self, x: int) -> None:
        if len(self.stk) == 0:
            self.stk.append((x, x))
        else:
            self.stk.append((x, max(x, self.stk[-1][1])))

    def pop(self) -> int:
        return self.stk.pop()[0]

    def top(self) -> int:
        return self.stk[-1][0]

    def peekMax(self) -> int:
        return self.stk[-1][1]

    def popMax(self) -> int:
        x = self.stk[-1][1]
        helper = []
        
        while self.stk[-1][0] != x:
            helper.append(self.pop()) # important, only append element
            
        self.pop()
            
        for elem in helper[::-1]:
            self.push(elem) # 关键，调用push方法
            
        return x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()