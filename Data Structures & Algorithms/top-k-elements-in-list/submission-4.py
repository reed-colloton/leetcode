class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        counts = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] += 1

        for num, count in freq.items():
            counts[count].append(num)

        top_k = []
        for i in range(len(counts) - 1, 0, -1):
            for num in counts[i]:
                top_k.append(num)
            if len(top_k) == k:
                return top_k
        
        return []
            