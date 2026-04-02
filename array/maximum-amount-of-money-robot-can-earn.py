class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])
        dp = [[[-float('inf'), -float('inf'), -float('inf')] for i in range(m)] for j in range(n)]
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0
        for i in range(1, n):
            dp[i][0][0] = dp[i-1][0][0] + coins[i][0]
            dp[i][0][1] = dp[i-1][0][1] + coins[i][0]
            if coins[i][0] < 0:
                dp[i][0][1] = max(dp[i][0][1], dp[i-1][0][0])
            dp[i][0][2] = dp[i-1][0][2] + coins[i][0]
            if coins[i][0] < 0:
                dp[i][0][2] = max(dp[i][0][2], dp[i-1][0][1])
        for j in range(1, m):
            dp[0][j][0] = dp[0][j-1][0] + coins[0][j]
            dp[0][j][1] = dp[0][j-1][1] + coins[0][j]
            dp[0][j][2] = dp[0][j-1][2] + coins[0][j]
            if coins[0][j] < 0:
                dp[0][j][1] = max(dp[0][j][1], dp[0][j-1][0])
                dp[0][j][2] = max(dp[0][j][2], dp[0][j-1][1])
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0]) + coins[i][j]
                dp[i][j][1] = max(dp[i-1][j][1], dp[i][j-1][1]) + coins[i][j]
                dp[i][j][2] = max(dp[i-1][j][2], dp[i][j-1][2]) + coins[i][j]
                if coins[i][j] < 0:
                    dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][0], dp[i][j-1][0])
                    dp[i][j][2] = max(dp[i][j][2], dp[i-1][j][1], dp[i][j-1][1])
        return max(dp[-1][-1])