class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        correct = range(1, len(nums)+1)
        for i in range(len(nums)+1):
            if nums[i] != correct[i]:
                return [nums[i], correct[i]]