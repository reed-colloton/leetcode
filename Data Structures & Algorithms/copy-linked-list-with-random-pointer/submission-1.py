"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_nodes = {}
        cur = head
        while cur:
            new_nodes[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            node = new_nodes[cur]
            node.next = new_nodes.get(cur.next)
            node.random = new_nodes.get(cur.random)
            cur = cur.next
        return new_nodes[head]
            