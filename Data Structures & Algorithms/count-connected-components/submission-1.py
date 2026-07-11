class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighboor in graph[node]:
                dfs(neighboor)

        components = 0
        for node in graph:
            if node in seen:
                continue
            components += 1
            dfs(node)
        return components