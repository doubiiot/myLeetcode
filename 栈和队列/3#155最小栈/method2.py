class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stk.append(x)
        self.min_stack.append(min(x,self.min_stack[-1]))

    def pop(self) -> None:
        self.stk.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stk[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
