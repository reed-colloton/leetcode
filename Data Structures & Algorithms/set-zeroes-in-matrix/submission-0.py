class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        for r in range(M):
            for c in range(N):
                if r in rows or c in cols:
                    matrix[r][c] = 0