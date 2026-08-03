class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, currSub=nums[0], 0
        for x in nums:
            if currSub<0:
                currSub=0
            currSub+=x
            maxSub=max(maxSub, currSub)
        return maxSub