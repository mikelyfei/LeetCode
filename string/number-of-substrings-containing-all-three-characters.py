class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = {"a": 0, "b":0, "c":0}
        n = len(s)
        l = 0
        ans = 0
        for r in range(n):
            cnt[s[r]] += 1
            while cnt['a']>0 and cnt['b']>0 and cnt['c']>0:
                ans += n-r
                cnt[s[l]] -= 1
                l += 1
                
        return ans