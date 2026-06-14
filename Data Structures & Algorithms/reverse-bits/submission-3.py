class Solution:
    def reverseBits(self, n: int) -> int:
        x = n
        new = 0x0
        for i in range(32):
            xi = x & 0x1
            x >>= 1
            new <<= 1
            new |= xi
        return new