class MyStack:
#使用单个队列实现
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        #can use popleft and append operation
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        length = len(self.q)
        self.q.append(x)
        for i in range(length):
            self.q.append(self.q.popleft())
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
