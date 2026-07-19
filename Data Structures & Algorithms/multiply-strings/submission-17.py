class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in (num1, num2):
            return '0'
        product = 0
        x_place = 1
        for x in reversed(num1):
            x = int(x)
            y_place = x_place
            for y in reversed(num2):
                y = int(y)
                product += x * y * y_place
                y_place *= 10
            x_place *= 10
        return str(product)