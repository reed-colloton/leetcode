class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        node = res = 0
        edges = 0
        dist = [float('inf') for _ in range(n)]
        seen = [False for _ in range(n)]

        while edges < n - 1:
            seen[node] = True
            nxt = -1
            for i in range(n):
                if seen[i]:
                    continue
                new_dist = (abs(points[i][0] - points[node][0]) + 
                            abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], new_dist)
                if nxt == -1 or dist[i] < dist[nxt]:
                    nxt = i
            res += dist[nxt]
            node = nxt
            edges += 1
        
        return int(res)
