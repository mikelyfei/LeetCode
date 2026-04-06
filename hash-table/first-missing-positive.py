class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [0]*(n+1)
        for i in range(n):
            if nums[i] < n+1:
                seen[nums[i]] = 1
        for i in range(1, n+1):
            if not seen[i]:
                return i
        return n+1