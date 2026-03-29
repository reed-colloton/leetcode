class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = {nums[l]}
        for r in range(1, len(nums)):
            if nums[r] in window:
                return True
            window.add(nums[r])
            if r - l >= k:
                window.remove(nums[l])
                l += 1
        return False