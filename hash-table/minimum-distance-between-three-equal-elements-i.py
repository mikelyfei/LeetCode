class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import defaultdict
        counter = defaultdict(list)
        for i in range(n):
            counter[nums[i]].append(i)
        ans = float('inf')
        for k, v in counter.items():
            if len(v) >= 3:
                for i in range(2, len(v)):
                    ans = min(abs(v[i]-v[i-1])+abs(v[i-1]-v[i-2])+abs(v[i]-v[i-2]), ans)
        return -1 if ans==float('inf') else ans