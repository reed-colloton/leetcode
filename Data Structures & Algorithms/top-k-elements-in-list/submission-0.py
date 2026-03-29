class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        top_k = [num for num, _ in sorted_freq][:k]
        return top_k
