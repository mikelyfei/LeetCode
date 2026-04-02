class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        maxNum = len(nums) 
        count = [0] * (maxNum + 1)
        for i in range(maxNum):
            if nums[i] <= maxNum:
                count[nums[i]] += 1
        for i in range(1, len(count)):
            if count[i] == 0:
                missing = i
            if count[i] == 2:
                duplicate = i
        return [duplicate, missing]