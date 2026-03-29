class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(1, len(height) - 1):
            total += max(0, min(max([0] + height[:i]), max(height[i:])) - height[i])
        return total