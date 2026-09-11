class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        flipped = 0
        for c in s:
            flipped ^= ord(c)
        for c in t:
            flipped ^= ord(c)
        return chr(flipped)