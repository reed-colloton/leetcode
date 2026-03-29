class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            match token:
                case '+':
                    nums.append(nums.pop() + nums.pop())
                case '-':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(a - b)
                case '*':
                    nums.append(nums.pop() * nums.pop())
                case '/':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(int(a / b))
                case _:
                    nums.append(int(token))
        return nums.pop()
                