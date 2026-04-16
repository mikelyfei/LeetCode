class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            j = i+1
            while j<len(nums) and j-i<=k:
                if nums[i]==nums[j]:
                    return True
                else:
                    j+=1
        return False     