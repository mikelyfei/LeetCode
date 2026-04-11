class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        ans = float('inf')
        for k, v in indices.items():
            if len(v) >=3:
                v.sort()
                for i in range(2, len(v)):
                    ans = min(ans, 2*abs(v[i] - v[i-2]))
        return ans if ans != float('inf') else -1