class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0
        n = len(s)
        ans=0
        max_freq = 0
        for r in range(n):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            max_freq = max(max_freq, cnt[s[r]])
            while r-l+1-max_freq>k:
                cnt[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
        return ans