class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges) - 1 + 1
        parents = [i for i in range(n + 1)]

        def find_root(node):
            while parents[node] != node:
                node = parents[node]
            return node
        
        def union(a, b):
            a_root = find_root(a)
            b_root = find_root(b)
            if a_root == b_root:
                return False
            parents[b_root] = a_root
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]