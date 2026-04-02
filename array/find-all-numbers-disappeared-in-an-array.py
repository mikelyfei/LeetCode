class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        unique_nums = set(nums)
        res = []
        for i in range(1, n+1):
            if i not in unique_nums:
                res.append(i)
        return res