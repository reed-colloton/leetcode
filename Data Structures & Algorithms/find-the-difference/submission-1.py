class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        flipped = 0
        for c in s + t:
            flipped ^= ord(c)
        return chr(flipped)