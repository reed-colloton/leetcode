class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = {}
        triplets = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0:
                        triple = sorted([nums[i], nums[j], nums[k]])
                        if triple not in triplets:
                            triplets.append(triple)
        return triplets