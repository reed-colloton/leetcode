class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        M, N = len(grid), len(grid[0])

        def dfs(r, c):
                    if (
                        r < 0 or c < 0 
                        or r == M or c == N 
                        or (r, c) in visited 
                        or grid[r][c] == '0'
                    ):
                        return
                    else:
                        visited.add((r, c))
                        dfs(r + 1, c)
                        dfs(r - 1, c)
                        dfs(r, c + 1)
                        dfs(r, c - 1)
    
        res = 0
        for r in range(M):
            for c in range(N):
                if (r, c) in visited:
                    continue
                
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                dfs(r, c)
        return res
