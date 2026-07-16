class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        traversal = []
        M, N = len(matrix), len(matrix[0])
        
        def circle(level):
            if 2 * level >= M or 2 * level >= N:
                return
            r, c = level, level
            width = N - level * 2 - 1
            height = M - level * 2 - 1
            traversal.append(matrix[r][c])
            for _ in range(width):
                c += 1
                traversal.append(matrix[r][c])
            if height == 0:
                return
            for _ in range(height):
                r += 1
                traversal.append(matrix[r][c])
            if width == 0:
                return
            for _ in range(width):
                c -= 1
                traversal.append(matrix[r][c])
            for _ in range(height - 1):
                r -= 1
                traversal.append(matrix[r][c])
            circle(level + 1)
        circle(0)
        return traversal
