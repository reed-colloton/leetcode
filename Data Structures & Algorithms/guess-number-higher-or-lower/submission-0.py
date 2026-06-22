# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.guessNumberHelper(0, n)

    def guessNumberHelper(self, l: int, r: int) -> int:
        x = l + (r - l) // 2
        if guess(x) == 0:
            return x
        elif guess(x) == 1:
            return self.guessNumberHelper(x + 1, r)
        else:
            return self.guessNumberHelper(l, x - 1)
