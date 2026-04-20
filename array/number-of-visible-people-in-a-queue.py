class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        ans = [0] * n

        for i in range(n-1, -1, -1):
            count = 0
            h = heights[i]
            while stack and stack[-1] < h:
                stack.pop()
                count += 1
            if stack:
                count += 1
            stack.append(h)
            ans[i] = count
        return ans