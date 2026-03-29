class Solution:
    def isValid(self, s: str) -> bool:
        closings = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c in closings:
                if not stack or stack.pop() != closings[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0