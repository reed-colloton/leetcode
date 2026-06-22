# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while True:
            x = l + (r - l) // 2
            placement = guess(x)
            if placement == 0:
                return x
            elif placement == 1:
                l = x + 1
            else:
                r = x - 1
