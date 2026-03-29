class Solution:
    def isValid(self, s: str) -> bool:
        openings = '({['
        closings = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c in openings:
                stack.append(c)
            if c in closings:
                if not stack or stack.pop() != closings[c]:
                    return False
        return len(stack) == 0