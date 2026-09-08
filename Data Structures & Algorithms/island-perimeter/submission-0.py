class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter = 0
        seen = set()

        def expand(r, c):
            if (r < 0 or c < 0 or 
                r >= len(grid) or c >= len(grid[0])
                or grid[r][c] == 0
            ):
                nonlocal perimeter
                perimeter += 1
                return
            if (r, c) in seen:
                return
            seen.add((r, c))
            expand(r + 1, c)
            expand(r - 1, c)
            expand(r, c + 1)
            expand(r, c - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    expand(r, c)
                    return perimeter
        # return 0