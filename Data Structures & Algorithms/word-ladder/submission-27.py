class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if beginWord == endWord:
            return 0
        
        words = set(wordList)
        
        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        m = len(beginWord)

        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step

            for i in range(m):
                for c in range(26):
                    char = chr(ord('a') + c)
                    neighbor = word[:i] + char + word[i + 1:]
                    if neighbor in words:
                        words.remove(neighbor)
                        queue.append((neighbor, step + 1))
        return 0
