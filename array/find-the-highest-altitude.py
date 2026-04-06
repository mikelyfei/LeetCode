class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        ans = 0
        for g in gain:
            
            prefix_sum += g
            ans = max(ans, prefix_sum)
        return ans