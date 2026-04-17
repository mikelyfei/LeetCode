class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        cnt = defaultdict(list)
        ans = float('inf')
        for i, num in enumerate(nums):
            cnt[num].append(i)
        for i, num in enumerate(nums):
            reversed_num = int(str(num)[::-1])
            if reversed_num in cnt:
                arr = cnt[reversed_num]
                candidates = [x for x in arr if x != i]
                j = min(candidates, key=lambda x: abs(x - i)) if candidates else None
                if j:
                    ans = min(ans, abs(i-j))
        return ans if ans!=float('inf') else -1