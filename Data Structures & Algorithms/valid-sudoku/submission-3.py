class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == '.':
                    continue
                if cell in rows[r] or cell in cols[c]:
                    return False
                box = (r // 3, c // 3)
                if cell in boxes[box]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[box].add(cell)
        return True
                