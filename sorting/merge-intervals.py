class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for start, end in intervals:
            if not ans or start>ans[-1][1]:
                ans.append([start, end])
            else:
                start = min(start, ans[-1][0])
                end = max(end, ans[-1][1])
                ans.append([start, end])
        return ans