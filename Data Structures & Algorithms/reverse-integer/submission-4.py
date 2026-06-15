class Solution:
    def reverse(self, x: int) -> int:
        sign = int(x < 0)
        x = abs(x)
        new = 0
        while x:
            new *= 10
            new += x % 10
            x = int(x / 10)
        if new > (2 ** 31 - 1):
            return 0
        return (-1) ** sign * new
