class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m = len(wordList[0])
        graph = {word : [] for word in wordList + [beginWord]}
        for word in graph:
            for i in range(m):
                for c in range(26):
                    char = chr(ord('a') + c)
                    neighboor = word[:i] + char + word[i + 1:]
                    if neighboor in graph:
                        graph[neighboor].append(word)

        queue = deque()
        visited = set()

        def bfs():
            if not queue:
                return 0
            word, step = queue.popleft()
            if word == endWord:
                return step
            if word not in visited:
                visited.add(word)
                for neighboor in graph[word]:
                    queue.append((neighboor, step + 1))
            return bfs()
        
        queue.append((beginWord, 1))
        return bfs()
