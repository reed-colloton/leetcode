class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        for i in range(len(heights)):
            l = i
            for j in range(i, -1, -1):
                if heights[j] < heights[i]:
                    break
                else:
                    l = j
            r = i
            for j in range(i, len(heights)):
                if heights[j] < heights[i]:
                    break
                else:
                    r = j
            largest = max(largest, heights[i] * (r - l + 1))
        return largest
