class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if 0<num<n+1:
                x = nums[num-1]
                nums[num-1] = num
                nums[i] = x
        for i in range(1,n+1):
            num = nums[i-1]
            if num>0 and num!=i:
                return i
        return n