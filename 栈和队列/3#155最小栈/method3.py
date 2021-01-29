#不使用辅助空间来做
#很强的方法
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_val = 0
    def push(self, x: int) -> None:
        if not self.stk:
            self.stk.append(0)
            self.min_val = x
        else:
            diff = x - self.min_val
            self.stk.append(diff)
            self.min_val = x if diff < 0 else self.min_val
    def pop(self) -> None:
        val = self.stk.pop()
        if val > 0:
            top = val + self.min_val
        else:
            top = self.min_val
            self.min_val -= val
    def top(self) -> int:
        val = self.stk[-1]
        return val + self.min_val if val > 0 else self.min_val

    def getMin(self) -> int:
        return self.min_val



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
