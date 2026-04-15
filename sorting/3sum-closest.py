class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)-2):
            two_sum_target = target - nums[i]
            for j in range(i+1, len(nums)-1):
                k = j+1
                while k<len(nums):
                    x = nums[i] + nums[j] + nums[k]
                    if abs(x-target) < abs(ans-target):
                        ans = x
                    if x<target:
                        k+=1
                    else:
                        break
        return ans