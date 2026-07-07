class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        graph = {i : [] for i in range(n)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighboor in graph[node]:
                dfs(neighboor)

        dfs(0)

        return len(seen) == n