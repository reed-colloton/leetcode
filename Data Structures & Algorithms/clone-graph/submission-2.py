"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copied = {}
        def dfs(node):
            if node in copied:
                return copied[node]
            copy = Node(val=node.val)
            copied[node] = copy
            copy.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            return copy
        return dfs(node)
