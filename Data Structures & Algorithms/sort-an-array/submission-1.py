class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        return self.sortArrayHelper(nums[:mid], nums[mid:])

    def sortArrayHelper(self, left: List[int], right: List[int]) -> List[int]:
        if len(left) > 1:
            mid_l = len(left) // 2
            left = self.sortArrayHelper(left[:mid_l], left[mid_l:])
        if len(right) > 1:
            mid_r = len(right) // 2
            right = self.sortArrayHelper(right[:mid_r], right[mid_r:])
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result