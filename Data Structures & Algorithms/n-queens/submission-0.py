class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        boards = []
        northwest = set()
        southwest = set()
        columns = set()

        def backtrack(r: int) -> None:
            if r == n:
                boards.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in columns or r + c in northwest or r - c in southwest: 
                    continue
                northwest.add(r + c)
                southwest.add(r - c)
                columns.add(c)
                board[r][c] = 'Q'
                backtrack(r + 1)
                board[r][c] = '.'
                northwest.remove(r + c)
                southwest.remove(r - c)
                columns.remove(c)

        board = [['.'] * n for _ in range(n)]
        backtrack(0)
        return boards
