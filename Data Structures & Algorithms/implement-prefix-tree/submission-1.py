class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_leaf = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] == None:
                cur.children[i] = Node()
            cur = cur.children[i]
        cur.is_leaf = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return cur.is_leaf


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True

        