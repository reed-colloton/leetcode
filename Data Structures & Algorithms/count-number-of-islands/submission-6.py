class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0 or c < 0 
                or r == M or c == N
                or grid[r][c] == '0'
            ):
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
    
        res = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        return res
