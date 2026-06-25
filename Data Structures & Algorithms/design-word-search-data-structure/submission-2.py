class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.root)

    def search_helper(self, word: str, i: int, node: Node) -> bool:
        if i == len(word):
            return node.is_end
        if word[i] == '.':
            return any(
                self.search_helper(word, i + 1, node)
                for node in node.children.values()
            )
        if word[i] not in node.children:
            return False
        node = node.children[word[i]]
        return self.search_helper(word, i + 1, node)
