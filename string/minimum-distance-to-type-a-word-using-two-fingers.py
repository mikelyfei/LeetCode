class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        dp = [[[0 for _ in range(26)] for _ in range(26)] for _ in range(n+1)]
        def dist(a, b):
            return abs(a//6-b//6)+abs(a%6-b%6)
        for i in range(n):
            t = ord(word[i]) - ord('A')
            for j in range(26):
                for k in range(26):
                    dp[i+1][j][k] = float('inf')
            for j in range(26):
                for k in range(26):
                    dp[i+1][j][t] = min(dp[i+1][j][t], dp[i][j][k] + dist(t, k))
                    dp[i+1][t][k] = min(dp[i+1][t][k], dp[i][j][k] + dist(j, t))
        return min(min(dp[-1]))