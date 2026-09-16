class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
    
    def _move(self) -> None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))

    def pop(self) -> int:
        self._move()
        return self.stack2.pop(-1)

    def peek(self) -> int:
        self._move()
        return self.stack2[-1]

    def empty(self) -> bool:
        self._move()
        return len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()