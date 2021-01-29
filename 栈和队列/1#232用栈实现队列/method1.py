class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.s1) == 0:
            self.front = x
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        for j in range(len(self.s2)):
            self.s1.append(self.s2.pop())
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        var = self.s1.pop()
        if len(self.s1) > 0:
            self.front = self.s1[-1]
        return var


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if len(self.s1) > 0 else True
# 入队O(N),出队O(1)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
