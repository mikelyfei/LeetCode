from typing import List
from collections import defaultdict
from bisect import bisect_right

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)

        for i, num in enumerate(nums):
            pos[num].append(i)

        ans = float("inf")

        for i, num in enumerate(nums):
            rev = int(str(num)[::-1])

            if rev not in pos:
                continue

            arr = pos[rev]

            # 找第一个 > i 的下标，保证 mirror pair 是 (i, j), i < j
            k = bisect_right(arr, i)

            if k < len(arr):
                j = arr[k]
                ans = min(ans, j - i)

        return ans if ans != float("inf") else -1