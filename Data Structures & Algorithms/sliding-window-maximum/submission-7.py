class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []        
        dq = collections.deque()
        l = 0
        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            if l > dq[0]:
                dq.popleft()
            if dq and r >= k - 1:
                res.append(nums[dq[0]])
                l += 1
        return res