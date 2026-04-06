class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd_prefix = []
        even_prefix = []
        op = 0
        ep = 0
        for i in range(n):
            if i%2:
                op += nums[i]
                odd_prefix.append(op)
            else:
                ep += nums[i]
                even_prefix.append(ep)
        ans = 0
        len_odd = len(odd_prefix)
        if even_prefix[-1] - nums[0] == odd_prefix[-1]:
            ans += 1
        for i in range(n):
            even_sum_before = even_prefix[i//2] - nums[i] if i%2==0 else even_prefix[i//2]
            odd_sum_before = odd_prefix[min(len_odd-1, i//2)] - nums[i] if i%2 else odd_prefix[min(len_odd-1,i//2)]
            even_sum_after = even_prefix[-1] - even_prefix[i//2]
            odd_sum_after = odd_prefix[-1] - odd_prefix[min(len_odd-1, i//2)]
            if even_sum_before + odd_sum_after == odd_sum_before + even_sum_after:
                ans += 1
        return ans