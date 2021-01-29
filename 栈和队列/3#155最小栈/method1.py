class MinStack:
#没有过，待看
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_num = 0
    def push(self, x: int) -> None:
        if not self.stk:
            self.min_num = x
        else:
            self.min_num = min(self.min_num, x)
        self.stk.append(x)

    def pop(self) -> None:
        val = self.stk.pop()
        if self.stk and val == self.min_num:
            self.min_num = self.stk[0]
            for i in range(len(self.stk)):
                self.min_num = min(self.min_num, self.stk[i])

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_num



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
