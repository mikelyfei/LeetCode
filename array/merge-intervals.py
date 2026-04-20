class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for start, end in intervals:
            if ans and start<=ans[-1][1]:
                start = min(start, ans[-1][0])
                end = max(end, ans[-1][1])
                ans[-1] = [start, end]
            else:
                ans.append([start, end])
        return ans