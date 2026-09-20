class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        red, white, blue = counts[0], counts[1], counts[2]
        for i in range(0, red):
            nums[i] = 0
        for i in range(red, red + white):
            nums[i] = 1
        for i in range(white + red, white + red + blue):
            nums[i] = 2
