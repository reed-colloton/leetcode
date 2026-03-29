import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
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