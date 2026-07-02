class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        M, N = len(heights), len(heights[0])

        def dfs(r, c):
            if r == 0 or c == 0:
                nonlocal pacific
                pacific = True
            if r == M - 1 or c == N - 1:
                nonlocal atlantic
                atlantic = True
            visited.add((r, c))
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                    nr >= 0 and nc >= 0 and
                    nr < M and nc < N and
                    (nr, nc) not in visited and 
                    heights[nr][nc] <= heights[r][c]
                ):
                    dfs(nr, nc)

        divides = []
        for r in range(M):
            for c in range(N):
                pacific = False
                atlantic = False
                visited = set()
                dfs(r, c)
                if atlantic and pacific:
                    divides += [[r, c]]
        return divides
