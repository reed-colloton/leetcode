class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest = 0
        row = 0
        for num in nums:
            if num == 1:
                row += 1
            else:
                row = 0
            highest = max(highest, row)
        return highest