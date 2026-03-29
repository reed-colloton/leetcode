class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_0 in enumerate(nums):
            for j, num_1 in enumerate(nums):
                if i == j:
                    pass
                elif num_0 + num_1 == target:
                    return [i, j]