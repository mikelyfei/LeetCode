class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        mod = total % p
        if mod == 0:
            return 0
        hashmap = {0:-1}
        prefix = 0
        ans = len(nums)
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p
            target = (prefix - mod) % p
            if target in hashmap:
                ans = min(ans, i-hashmap[target])
            hashmap[prefix] = i
        return ans
        
        
        
        