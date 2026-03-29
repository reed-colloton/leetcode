class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)
        while l < r:
            sum = numbers[l - 1] + numbers[r - 1]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l, r]