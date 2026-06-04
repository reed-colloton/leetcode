class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0]) if board else 0
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r >= M or r < 0
                    or c >= N or c < 0
                    or word[i] != board[r][c]
                    or (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1)
                    or dfs(r - 1, c, i + 1)
                    or dfs(r, c + 1, i + 1)
                    or dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False