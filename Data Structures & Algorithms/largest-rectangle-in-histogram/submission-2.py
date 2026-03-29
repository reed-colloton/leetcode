class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > h:
                j, h2 = stack.pop()
                largest = max(largest, h2 * (i - j))
                start = j
            stack.append((start, h))
        return largest