class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen = []
            for j in range(9):
                x = board[i][j]
                if x == '.':
                    continue
                if x in seen:
                    return False
                seen.append(x)

        for i in range(9):
            seen = []
            for j in range(9):
                x = board[j][i]
                if x == '.':
                    continue
                if x in seen:
                    return False
                seen.append(x)

        for offset_i in range(3):
            for offset_j in range(3):
                seen = []
                for i in range(3):
                    for j in range(3):
                        x = board[offset_i * 3 + i][offset_j * 3 + j]
                        if x == '.':
                            continue
                        if x in seen:
                            return False
                        seen.append(x)
        return True
