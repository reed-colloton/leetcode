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
                if cell in rows[r]:
                    return False
                if cell in cols[c]:
                    return False
                if cell in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[(r // 3, c // 3)].add(cell)
        return True
                