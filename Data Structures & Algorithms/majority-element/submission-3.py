import math
import random

class Solution:
    def voting(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                 freq[num] = 1
        most = {'num': None, 'occurrences': -math.inf}
        for num in freq.keys():
            if most['occurrences'] < freq[num]:
                most['num'] = num
                most['occurrences'] = freq[num]
        return most['num']

    def random(self, nums: List[int]) -> int:
        while True:
            i = random.randint(0, len(nums) - 1)
            count = nums.count(nums[i])
            if count > len(nums) // 2:
                return nums[i]

    majorityElement = random
