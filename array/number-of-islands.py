class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]=="0":
                return 0
            grid[i][j] = "0"
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                dfs(x, y)
            return 1
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += dfs(i, j)
        return cnt