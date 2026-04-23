class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        arr = [0] * len(nums)
        for num, idx_list in pos.items():
            n = len(idx_list)
            prefix = [0]*(n+1)
            for i in range(n):
                prefix[i+1]=prefix[i]+idx_list[i]
            for i, idx in enumerate(idx_list):
                left = idx*i-prefix[i]
                right = prefix[n]-prefix[i+1]-idx*(n-i-1)
                arr[idx]=left+right
        return arr