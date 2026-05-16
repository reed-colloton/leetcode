class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))
            while q:
                i, j = q.popleft()
                adj = set()
                adj.add((i, min(j + 1, cols - 1)))
                adj.add((i, max(j - 1, 0)))
                adj.add((min(i + 1, rows - 1), j))
                adj.add((max(i - 1, 0), j))
                for i, j in adj:
                    if grid[i][j] == '1' and (i, j) not in visited:
                        q.append((i, j))
                        visited.add((i, j))

        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited:
                    continue
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands

