class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.is_end = True
        M, N = len(board), len(board[0])
        res, visited = set(), set()
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                r >= M or c >= N or
                (r, c) in visited or 
                board[r][c] not in node.children
            ):
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_end:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))
        for r in range(M):
            for c in range(N):
                dfs(r, c, root, '')
        return list(res)

    
