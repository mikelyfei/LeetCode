class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            j = min(i+k, len(nums)-1)
            while j>i:
                if nums[i]==nums[j]:
                    return True
                else:
                    j-=1
        return False     