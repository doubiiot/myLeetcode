class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        #can use popleft and append operation
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.popleft()
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.q1 else True
#入栈 O(N) 出栈O(1)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
