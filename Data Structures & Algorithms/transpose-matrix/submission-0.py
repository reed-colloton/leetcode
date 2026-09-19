class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        new = [[0] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                new[c][r] = matrix[r][c]
        
        return new
