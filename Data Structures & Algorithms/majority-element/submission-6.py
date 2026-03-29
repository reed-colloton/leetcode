import math
import random

class Solution:
    def voting(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

    def random(self, nums: List[int]) -> int:
        while True:
            i = random.randint(0, len(nums) - 1)
            count = nums.count(nums[i])
            if count > len(nums) // 2:
                return nums[i]

    majorityElement = voting
