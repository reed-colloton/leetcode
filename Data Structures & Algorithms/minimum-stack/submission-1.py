import math


class ListNode:
    def __init__(self, value):
        self.value : int = value
        self.next : ListNode | None = None

class MinStack:
    def __init__(self):
        self.stack : ListNode | None = None

    def push(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.stack
        self.stack = node
        
    def pop(self) -> None:
        assert self.stack is not None
        self.stack = self.stack.next

    def top(self) -> int:
        assert self.stack is not None
        return self.stack.value
        

    def getMin(self) -> int:        
        assert self.stack is not None
        smallest = self.stack.value
        node = self.stack.next
        while node and node.value is not None:
            smallest = min(smallest, node.value)
            node = node.next
        assert type(smallest) is int
        return smallest
        
