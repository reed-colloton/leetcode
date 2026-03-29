class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        largest = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                j, h2 = stack.pop()
                largest = max(largest, h2 * (i - j))
                start = j
            stack.append((start, h))
        return largest