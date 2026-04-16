class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        ans = []
        n = len(nums)
        for q in queries:
            num = nums[q]
            idx = indices[num]
            if len(idx) == 1:
                ans.append(-1)
                continue
            pos = idx.index(q)  
            
            prev_idx = idx[(pos - 1) % len(idx)]
            next_idx = idx[(pos + 1) % len(idx)]
            
            d1 = min((q - prev_idx) % n, (prev_idx - q) % n)
            d2 = min((q - next_idx) % n, (next_idx - q) % n)
            
            ans.append(min(d1, d2))
        return ans
