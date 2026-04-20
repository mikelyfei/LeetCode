class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        from collections import deque
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if not fresh:
            return 0

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        t = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0<=x<m and 0<=y<n and grid[x][y]==1:
                        q.append((x, y))
                        grid[x][y] = 2
                        fresh -= 1
            t += 1
        return t if fresh==0 else -1
                    