class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap:
                for j in hashmap[num]:
                    print(hashmap[num])
                    print(abs(i - j))
                    if abs(i - j) <= k:
                        return True
                hashmap[num].append(i)
            else:
                hashmap[num] = [i]
        return False