class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for ui, vi, ti in times:
            ui -= 1
            vi -= 1
            graph[ui].append((ti, vi))

        seen = [float('inf')] * n
        queue = [(0, k - 1)]
        heapq.heapify(queue)

        while queue:
            elapsed, node = heapq.heappop(queue)
            print(elapsed, node)
            if elapsed < seen[node]:
                seen[node] = elapsed
                for dist, neighbor in graph[node]:
                    heapq.heappush(queue, (elapsed + dist, neighbor))

        time = max(seen)
        if time == float('inf'):
            return -1
        return int(time)
