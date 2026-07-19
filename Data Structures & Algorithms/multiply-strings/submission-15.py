class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in (num1, num2):
            return '0'
        product = 0
        for i, x in enumerate(reversed(num1)):
            x = int(x)
            for j, y in enumerate(reversed(num2)):
                y = int(y)
                product += x * y * 10 ** (i + j)
        return str(product)