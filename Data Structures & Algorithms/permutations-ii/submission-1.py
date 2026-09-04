class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        permutations = []
        current = []
        def backtrack():
            if len(current) == len(nums):
                permutations.append(current.copy())
                return
            for num in counts:
                if not counts[num]:
                    continue
                current.append(num)
                counts[num] -= 1
                backtrack()
                current.pop()
                counts[num] += 1
        backtrack()
        return permutations