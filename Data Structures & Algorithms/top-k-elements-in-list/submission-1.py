from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        asc = [k for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)]
        return asc[:k]
