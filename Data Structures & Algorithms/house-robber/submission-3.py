class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        score = [0] * n
        for i in range(n):
            score[i] = max(score[i - 1], nums[i] + score[i - 2])

        return max(score[n - 1], score[n - 2])
