import math


class ListNode:
    def __init__(self, value=None):
        self.value : int | None = value
        self.next : ListNode | None = None

class MinStack:
    def __init__(self):
        self.stack = ListNode()

    def push(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.stack
        self.stack = node
        
    def pop(self) -> None:
        assert self.stack is not None
        self.stack = self.stack.next

    def top(self) -> int:
        assert self.stack is not None
        assert self.stack.value is not None
        return self.stack.value
        

    def getMin(self) -> int:
        smallest = math.inf
        node = self.stack
        assert node is not None
        while node.next and node.value is not None:
            smallest = min(smallest, node.value)
            node = node.next
        return smallest
        
