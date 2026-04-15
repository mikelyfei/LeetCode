class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)-2):
            two_sum_target = target - nums[i]
            j = i+1
            k = len(nums) - 1
            while j<k<len(nums):
                x = nums[i] + nums[j] + nums[k]
                if abs(x-target) < abs(ans-target):
                    ans = x
                if x<target:
                    j+=1
                elif x == target:
                    return x
                else:
                    k -= 1
                    
        return ans