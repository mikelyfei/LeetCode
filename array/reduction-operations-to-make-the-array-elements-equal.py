class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:
                cnt+=1
            ans+=cnt        
        return ans
