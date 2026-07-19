class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in (num1, num2):
            return '0'
        x_digits = [int(x) for x in reversed(num1)]
        y_digits = [int(y) for y in reversed(num2)]
        product = 0
        x_place = 1
        for x in x_digits:
            y_place = x_place
            for y in y_digits:
                product += x * y * y_place
                y_place *= 10
            x_place *= 10
        return str(product)