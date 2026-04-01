class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        res = 0
        for left in range(n):
            if nums[left] == 0:
                continue
            right = left
            while right < n and nums[right] == 1:
                right += 1
                res = max(res, right-left)
        return res