class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 1
        while r < len(nums):
            if r - l > k:
                l += 1
            print(l, r)
            if nums[r] in nums[l:r]:
                return True
            r += 1
        return False