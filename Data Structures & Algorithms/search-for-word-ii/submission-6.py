class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        M, N = len(board), len(board[0])
        res, visited = set(), set()
        def dfs(r, c, node):
            if (r < 0 or c < 0 or 
                r >= M or c >= N or
                (r, c) in visited or 
                board[r][c] not in node.children
            ):
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            if node.word:
                res.add(node.word)
                node.word = None
            dfs(r + 1, c, node)
            dfs(r, c + 1, node)
            dfs(r - 1, c, node)
            dfs(r, c - 1, node)
            visited.remove((r, c))
        for r in range(M):
            for c in range(N):
                dfs(r, c, root)
        return list(res)
