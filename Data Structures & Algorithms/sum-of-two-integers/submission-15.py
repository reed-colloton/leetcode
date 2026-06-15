class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        carry = 0x0
        place = 0x1
        new = 0x0
        while a or b or carry:
            x1 = a & 0x1
            x2 = b & 0x1
            y = x1 ^ x2 ^ carry
            carry = x1 & x2 | (x1 | x2) & carry
            if y:
                new |= place
            place <<= 1
            a >>= 1
            b >>= 1
        new &= 0xFFFFFFFF
        if new > 0x7FFFFFFF:
            return ~(new ^ 0xFFFFFFFF)
        return new
