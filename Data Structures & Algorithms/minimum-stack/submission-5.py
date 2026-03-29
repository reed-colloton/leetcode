class ListNode:
    def __init__(self, value):
        self.value : int = value
        self.next : ListNode | None
        self.least : int


class MinStack:
    def __init__(self):
        self.stack : ListNode | None = None


    def push(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.stack
        if self.stack:
            node.least = min(node.value, self.stack.least)
        else:
            node.least = node.value
        self.stack = node
        

    def pop(self) -> None:
        assert self.stack is not None
        self.stack = self.stack.next


    def top(self) -> int:
        assert self.stack is not None
        return self.stack.value
        

    def getMin(self) -> int:        
        assert self.stack is not None
        return self.stack.least
        
