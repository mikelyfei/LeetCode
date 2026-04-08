class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            l, r, k, v = q
            while l<=r:
                nums[l]=(nums[l]*v)%(10e9+7)
                l+=k
        ans = 0
        for num in nums:
            ans = int((ans^int(num))%(10e9+7))
        return ans