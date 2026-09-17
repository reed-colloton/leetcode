class Solution:
    def romanToInt(self, s: str) -> int:
        to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ints = [to_int[c] for c in list(s)]
        total = 0
        for i in range(len(ints)):
            if i == len(ints) - 1 or ints[i] >= ints[i + 1]:
                total += ints[i]
            else:
                total -= ints[i]
        return total