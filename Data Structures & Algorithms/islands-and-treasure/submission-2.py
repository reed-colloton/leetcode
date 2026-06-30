class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N = len(grid), len(grid[0])
        queue = deque()
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    dr == M or dc == N or
                    dr < 0 or dc < 0 or
                    grid[dr][dc] != 2147483647 # inf
                ):
                    continue
                grid[dr][dc] = grid[r][c] + 1
                queue.append((dr, dc))
        