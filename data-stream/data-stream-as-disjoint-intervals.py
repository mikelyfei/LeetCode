from bisect import bisect_left

class SummaryRanges:

    def __init__(self):
        self.intervals = []        

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        new_interval = [value, value]
        i = bisect_left(intervals, new_interval)
        if i > 0 and intervals[i-1][1] + 1 >= value:
            i -= 1
        while i < len(intervals) and intervals[i][0] - 1 <= new_interval[1]:
            new_interval[0] = min(intervals[i][0], new_interval[0])
            new_interval[1] = max(intervals[i][1], new_interval[1])
            intervals.pop(i)
        intervals.insert(i, new_interval)


    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()