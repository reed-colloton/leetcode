class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])

        zero_first_row = False
        for c in range(N):
            if matrix[0][c] == 0:
                zero_first_row = True
                break

        for r in range(1, M):
            for c in range(N):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, M):
            for c in range(1, N):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0: # zero_first_col
            for r in range(M):
                matrix[r][0] = 0

        if zero_first_row:
            for c in range(N):
                matrix[0][c] = 0


