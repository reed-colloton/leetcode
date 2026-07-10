class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber > 0:
            columnNumber -= 1
            digit = columnNumber % 26
            title.append(chr(ord('A') + digit))
            columnNumber //= 26
        title.reverse()
        return ''.join(title)