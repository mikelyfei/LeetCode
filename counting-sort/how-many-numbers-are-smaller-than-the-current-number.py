class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        n = len(nums)
        res = []
        counter = {}
        for i in range(n):
            if sorted_nums[i] not in counter:
                counter[sorted_nums[i]] = i
        for i in range(n):
            res.append(counter[nums[i]])
        return res
