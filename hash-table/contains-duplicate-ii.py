class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_pos = {}
        for i, num in enumerate(nums):
            if num in last_pos and i-last_pos[num]<=k:
                return True
            last_pos[num] = i
        return False     