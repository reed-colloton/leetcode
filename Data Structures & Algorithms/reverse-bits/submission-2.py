class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        steps = 32
        while n:
            x = n & 1
            rev <<= 1
            rev |= x
            n >>= 1
            steps -= 1
        return rev << steps