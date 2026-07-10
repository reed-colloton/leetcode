class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ''
        while columnNumber > 26:
            digit = columnNumber % 26
            print(digit)
            title = chr(ord('A') + digit - 1) + title
            columnNumber //= 26
        title = chr(ord('A') + columnNumber - 1) + title
        return title