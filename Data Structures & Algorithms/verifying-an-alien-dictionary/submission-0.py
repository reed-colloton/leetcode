class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {c: chr(ord('a') + i) for i, c in enumerate(order)}
        english = [''.join([mapping[c] for c in word]) for word in words]
        return sorted(english) == english