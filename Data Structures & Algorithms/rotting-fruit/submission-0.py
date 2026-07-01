class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        M, N = len(grid), len(grid[0])
        for r in range(M):
            for c in range(N):
                cell = grid[r][c]
                if cell == 1:
                    fresh += 1
                elif cell == 2:
                    queue.append((r, c))
        queue.append((-1, -1))
        mins = 0
        while queue:
            r, c = queue.popleft()
            if r == c == -1:
                if not queue:
                    break
                mins += 1
                queue.append((-1, -1))
                continue
            for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                    dr >= 0 and dc >= 0 and
                    dr < M and dc < N and
                    grid[dr][dc] == 1
                ):
                    fresh -= 1
                    grid[dr][dc] = 2
                    queue.append((dr, dc))
        if fresh != 0:
            return -1
        return mins