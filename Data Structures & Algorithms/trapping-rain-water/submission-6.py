class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(1, len(height) - 1):
            total += min(max(height[:i + 1]), max(height[i:])) - height[i]
        return total