class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL = maxR = total = 0
        while l < r:
            if height[l] <= height[r]:
                maxL = max(maxL, height[l])
                total += maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                total += maxR - height[r]
                r -= 1
        return total

    def trapPrefix(self, height: List[int]) -> int:
        lefts = [0] * len(height)
        lefts[0] = height[0]
        for i in range(1, len(height)):
            lefts[i] = max(lefts[i - 1], height[i])
        rights = [0] * len(height)
        rights[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            rights[i] =  max(rights[i + 1], height[i])
        total = 0
        for i in range(1, len(height) - 1):
            total += min(lefts[i], rights[i]) - height[i]
        return total
    