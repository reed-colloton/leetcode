class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r == M or c == N or
                grid[r][c] == 0
            ):
                return 0
            nonlocal size
            size += 1
            grid[r][c] = 0
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        M, N = len(grid), len(grid[0])
        res = 0
        for r in range(M):
            for c in range(N):
                size = 0
                dfs(r, c)
                res = max(res, size)
        return res