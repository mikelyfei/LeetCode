class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        next_smaller_stack = []
        last_smaller_stack = []
        n = len(heights)
        next_smaller = [n] * n 
        last_smaller = [-1] * n
        maxArea = 0
        for i, h in enumerate(heights):
            while next_smaller_stack and heights[next_smaller_stack[-1]] > h:
                next_smaller[next_smaller_stack.pop()] = i
            while last_smaller_stack and heights[last_smaller_stack[-1]] > heights[n-1-i]:
                last_smaller[last_smaller_stack.pop()] = n-1-i
            next_smaller_stack.append(i)
            last_smaller_stack.append(n-1-i)
        for i in range(n):
            maxArea = max((next_smaller[i] - last_smaller[i]-1)*heights[i], maxArea)
        return maxArea