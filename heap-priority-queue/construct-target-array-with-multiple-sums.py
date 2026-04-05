class Solution:
    def isPossible(self, target: List[int]) -> bool:
        import heapq
        s = sum(target)
        target = [-t for t in target]
        heapq.heapify(target)
        while target:
            largest = -heapq.heappop(target)
            if largest == 1:
                return True
            rest_s = s - largest
            largest -= rest_s
            s -= rest_s
            if largest <= 0:
                return False
            heapq.heappush(target, -largest)

