class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        traversal = []
        M, N = len(matrix), len(matrix[0])
        level = 0
        
        while 2 * level < M and 2 * level < N:
            r, c = level, level
            width = N - level * 2 - 1
            height = M - level * 2 - 1
            traversal.append(matrix[r][c])
            for _ in range(width):
                c += 1
                traversal.append(matrix[r][c])
            if height == 0:
                break
            for _ in range(height):
                r += 1
                traversal.append(matrix[r][c])
            if width == 0:
                break
            for _ in range(width):
                c -= 1
                traversal.append(matrix[r][c])
            for _ in range(height - 1):
                r -= 1
                traversal.append(matrix[r][c])
            level += 1
        return traversal