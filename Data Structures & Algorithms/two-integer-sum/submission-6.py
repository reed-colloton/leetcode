class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffs:
                diffs[diff].append(i)
            else:
                diffs[diff] = [i]
        for i, num in enumerate(nums):
            if num in diffs:
                for j in diffs[num]:
                    if i != j:
                        return [i, j]
        return [0, 0]