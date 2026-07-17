class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        m = len(beginWord)

        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step

            for i in range(m):
                for c in range(26):
                    neighbor = word[:i] + chr(ord('a') + c) + word[i + 1:]
                    if neighbor in words:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, step + 1))
        return 0
