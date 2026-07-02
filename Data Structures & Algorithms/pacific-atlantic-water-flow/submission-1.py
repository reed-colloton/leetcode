class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        M, N = len(heights), len(heights[0])
        queue = deque()

        # Pacific
        for r in range(M):
            queue.append((r, 0))
        for c in range(N):
            queue.append((0, c))
        pacific = set(queue)
        while queue:
            r, c = queue.popleft()
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                    nr >= 0 and nc >= 0 and
                    nr < M and nc < N and
                    (nr, nc) not in pacific and
                    heights[nr][nc] >= heights[r][c]
                ):
                    queue.append((nr, nc))
                    pacific.add((nr, nc))

        # Atlantic
        for r in range(M):
            queue.append((r, N - 1))
        for c in range(N):
            queue.append((M - 1, c))
        atlantic = set(queue)
        while queue:
            r, c = queue.popleft()
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                    nr >= 0 and nc >= 0 and
                    nr < M and nc < N and
                    (nr, nc) not in atlantic and
                    heights[nr][nc] >= heights[r][c]
                ):
                    queue.append((nr, nc))
                    atlantic.add((nr, nc))
            
        return list(atlantic & pacific)
        