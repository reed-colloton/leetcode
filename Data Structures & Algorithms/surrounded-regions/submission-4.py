class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        M, N = len(board), len(board[0])
        zeros = []

        for r in range(M):
            for c in range(N):
                if board[r][c] == 'O':
                    zeros += [(r, c)]
        
        visited = set()
        region = set()

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r == M or c == N or
                (r, c) in visited or
                board[r][c] == 'X'
            ):
                return True
            visited.add((r, c))
            region.add((r, c))
            surrounded = True
            if r in (0, M - 1) or c in (0, N - 1):
                surrounded = False
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if not dfs(nr, nc):
                    surrounded = False
            return surrounded
        
        for r, c in zeros:
            region = set()
            if dfs(r, c):
                for nr, nc in region:
                    board[nr][nc] = 'X'
