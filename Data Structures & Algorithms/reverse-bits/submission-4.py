class Solution:
    def reverseBits1(self, n: int) -> int:
        new = 0x0
        for i in range(32):
            xi = n & 0x1
            n >>= 1
            new <<= 1
            new |= xi
        return new
    def reverseBits(self, n: int) -> int:
        s = f'{n:032b}'
        s = s[::-1]
        return int(s, 2)