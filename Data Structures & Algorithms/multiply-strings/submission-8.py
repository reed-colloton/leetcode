class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        for i in range(len(num1)):
            x = int(num1[len(num1) - i - 1])
            for j in range(len(num2)):
                y = int(num2[len(num2) - j - 1])
                product += x * y * (10 ** i * 10 ** j)
                
        return str(product)