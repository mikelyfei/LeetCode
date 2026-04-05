class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            element = self.stack1.pop()
            self.stack2.append(element)
        element = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return element

    def peek(self) -> int:
        while self.stack1:
            element = self.stack1.pop()
            self.stack2.append(element)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return element


    def empty(self) -> bool:
        if self.stack1:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()