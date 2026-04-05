class Solution:
    def isPossible(self, target: List[int]) -> bool:
        import heapq
        s = sum(target)
        target = [-t for t in target]
        heapq.heapify(target)
        while True:
            largest = -heapq.heappop(target)                        
            rest_s = s - largest

            if largest == 1 or rest_s == 1:
                return True

            if largest <= rest_s or rest_s == 0:
                return False
            
            prev = largest % rest_s
            if prev == 0:
                return False
            s = rest_s + prev

            heapq.heappush(target, -prev)

